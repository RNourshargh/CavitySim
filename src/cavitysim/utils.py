import numpy as np


import copy


class Cavity(object):
    """An optical resonator.

    Attributes:
        elements: a list of optical elements (class objects) defining the cavity
        linear: Boolean to indicate if the cavity is linear or standing wave. (Linear cavities must be defined from an end mirror)
        n0: Refractive index of free space, default=1
    """

    def __init__(self, input_elements, linear, wavelength = 780e-9, n0=1):
        self.input_elements = input_elements
        self.linear = linear
        self.n0 = n0
        self.unfolded = False
        self.elements = copy.deepcopy(input_elements)
        self.wavelength = wavelength
        self.unfold()

    def unfold(self):
        """Unfold linear cavities"""
        # Check the cavity is linear and hasn't been unfolded
        if self.linear and not self.unfolded:
            self.returntrip = self.elements[1:-1]  # Slice off the end mirrors
            self.returntrip.reverse()  # reverse order of optical elements for the return trip
            self.elements.extend(
                self.returntrip
            )  # Add the reverse trip optics to the elements list
            self.unfolded = True  # Record that the cavity has been unfolded
        else:
            self.unfolded = True

    def abcd(self):
        """Generates the abcd matrix for the cavity, Be cautious in linear cavities with thick lenses"""

        elements_abcd_list = []  # Initialise list of abcd matrices
        elements_list = self.elements

        for element in elements_list:
            elements_abcd_list.append(element.abcd())  # populate list of abcd matrices

        abcd_matrix = np.identity(2)  # Initialise cavity abcd matrix
        for matrix in elements_abcd_list:
            abcd_matrix = np.matmul(
                abcd_matrix, matrix
            )  # multiply element abcd matrices together

        return abcd_matrix

    def abcd_shift(self, n=1):
        """Generates the abcd matrix for the cavity, shifted by n elements from it's start"""

        abcd_list = []  # Initialise list of abcd matrices
        elements_list = self.elements  # set that list equal to the input elements

        for element in elements_list:
            abcd_list.append(element.abcd())  # populate list of abcd matrices]

        indexlist = []  # generate a new list for the indicies

        for i in range(len(elements_list)):
            indexlist.append(
                i
            )  # fill index list with the indicies in their original order

        newindexlist = Cavity.reindex(indexlist, n)  # reorder the index list

        shifted_abcd_list = [
            abcd_list[i] for i in newindexlist
        ]  # generate an abcd list with the shifted indicies

        abcd_matrix = np.identity(2)  # Initialise cavity abcd matrix
        for matrix in shifted_abcd_list:
            abcd_matrix = np.matmul(
                abcd_matrix, matrix
            )  # multiply element abcd matrices together

        return abcd_matrix

    def reindex(list, n=1):
        newlist = list[n:] + list[:n]
        return newlist

    def ad(self):
        """Returns the trace of the ABCD matrix. The cavity is stable if this is between -2 and 2"""
        return np.trace(self.abcd())

    def stable(self):
        """Returns a boolean to indicate if the cavity is stable or not"""
        AD = self.ad()
        if (AD <= 2) and (AD >= -2):
            CavStab = True
        else:
            CavStab = False
        return CavStab

    def properties(self):
        if self.stable():
            print("Cavity is stable")
        else:
            print("Cavity is unstable")

        print("A+D = {}".format(self.ad()))
        print(self.abcd())
        print(self.end_radius())
        return

    def end_radius(self):
        """Returns the radius of the circulating beam in the transverse plane from which the cavity is defined"""
        m = self.ad() / 2
        abcd = self.abcd()
        B = abcd[0, 1]
        w = np.sqrt(abs(B) * self.wavelength / (np.pi) * np.sqrt(1 / (1 - m ** 2)))
        return w

    def Eigenvals(self):
        m = self.ad() / 2
        EigenA = m + np.sqrt(m ** 2 - 1 + 0j)
        EigenB = m - np.sqrt(m ** 2 - 1 + 0j)
        return EigenA, EigenB

    def GouyPhase(self):
        m = self.ad() / 2
        abcd = self.abcd()
        B = abcd[0, 1]
        Theta = np.sign(B) * np.arccos(m)
        if Theta < 0 :
            Theta += 2 * np.pi
        return Theta

    def radii_list(self):
        """Loops over the list of cavity elements and caculates the waist at each of them"""
        elementlist = copy.deepcopy(self.elements)

        self.radii_list_out = []

        for i in range(len(elementlist)):
            loopabcd = self.abcd_shift(n=i)
            self.radii_list_out.append(radius_from_abcd(loopabcd, self.wavelength))

        return self.radii_list_out
    
    def q_stableMode(self):
        """Calculates the q value for the stable eigenemode at the plane the abcd matrix is defined were one exists."""
        m = self.ad() / 2
        abcd = self.abcd()
        A = abcd[0, 0]
        B = abcd[0, 1]
        C = abcd[1, 0]
        D = abcd[1, 1]
        q = 1 / ((D-A)/2*B + 1j*np.sqrt(1-m**2)/abs(B) )
        return q


class LensThinVac(object):
    """A thin lens in a vacuum

    Attributes:
        f: focal length (metres)
    """

    def __init__(self, f):
        self.f = f

    def abcd(self):
        """Generate the abcd matrix for the thin lens"""
        return np.array([[1, 0], [-1 / (self.f), 1]])

    def opl(self):
        """Calculate the optical path length for the thin lens"""
        return 0


class PathConstantIndex(object):
    """Propagation through a path of refractive index n

    Attributes:
        d: path length (metres)
        n: refractive index, default n=1
        R: Reflectivity or reflectance, check if amplitude or power and units
        A: Absorbtion or absorbance, check if amplitude or power and units, or if I should be using transmission coefficients
    """

    def __init__(self, d, n=1, R=0, A=0):
        self.d = d
        self.n = n
        self.R = R
        self.A = A

    def abcd(self):
        """Returns the abcd matrix for the propagation, Using Siegman's convention which requires corrections to ROCs curvatures, when measured in a material with n>1, see pages 585 and 784"""
        return np.array([[1, self.d / self.n], [0, 1]])

    def opl(self):
        """Returns the optical path length for this propagation"""
        return self.d * self.n


class MirrorNormal(object):
    """Reflection from a mirror of ROC R, (R>0 for concave mirrors)

    Attributes:
        roc: Radius of curvature (metres), Default infinite (planar mirror)

    """

    def __init__(self, roc=np.inf):
        self.roc = roc

    def abcd(self):
        """Returns abcd matrix for reflection from this mirror"""
        return np.array([[1, 0], [-2 / self.roc, 1]])

    def opl(self):
        """returns the optical path length for reflection, 0"""
        return 0


def legacy_path_constant_index(path_length, n0):
    """
    generate the abcd matrix for propagation in a medium of constant refractive index
    """
    abcd = np.array([[1, path_length], [0, 1]])
    opl = n0 * path_length
    return abcd, opl


def rayleigh_range_w0(w0, wavelength=780e-9):
    """
    Calculate Rayleigh Range from waist w0
    """
    zr = np.pi * w0 ** 2 / wavelength
    return zr


def radius_from_abcd(abcd, wavelength):
    """
    Calculates the 1/e^2 radius from an abcd matrix and a wavelenth inside an optical cavity
    """
    m = np.trace(abcd) / 2
    B = abcd[0, 1]
    w = np.sqrt(abs(B) * wavelength / (np.pi) * np.sqrt(1 / (1 - m ** 2)))
    return w


def radius_from_q(q, wavelength=780e-9):
    """
    Calculates the beam radius w from q the complex beam parameter at the point q is definied
    """
    return np.sqrt(-wavelength / (np.pi * np.imag(1 / q)))

def roc_from_q(q, wavelength=780e-9):
    """
    Calculates the beam roc R from q the complex beam parameter at the point q is definied
    """
    return 1 / np.real(1 / q)


def legacy_lens_thin_vacuum_abcd(f):
    """
    Generates abcd matrix, for thin lens, focal length f (metres)
    """
    abcd = np.array([[1, 0], [-1 / f, 1]])
    opl = 0  # By definition for a thin lens
    return abcd, opl


def legacy_mirror_planar_normal():
    """
    Generates abcd matrix, for planar mirror at normal insidence
    """
    abcd = np.array([[1, 0], [0, 1]])
    opl = 0  # By definition for a planar mirror
    return abcd, opl


def abcd_stability(abcd):
    """
    Tests stability of a cavity defined by an abcd matrix.
    """
    AD = np.trace(abcd)
    if (AD <= 2) and (AD >= -2):
        print("Cavity is stable")
        CavStab = True
    else:
        print("Cavity is unstable")
        CavStab = False

    print("A+D = {}".format(AD))
    return AD, CavStab


def abcd_transform(abcd, q0):
    """Applied an abcd transformation to a complex beam parameter q"""
    A = abcd[0, 0]
    B = abcd[0, 1]
    C = abcd[1, 0]
    D = abcd[1, 1]
    q = (A * q0 + B) / (C * q0 + D)
    return q


# def PE_Lossless_Mirror_Coefficients(Int_Reflectance):
# """
# Calculates the amplitude and power reflection and transmission coefficients from the power reflectance for a lossless mirror
# """
# amp_reflectance = np.sqrt(Int_Reflectance)
# Int_Transmission = 1 - Int_Reflectance
# amp_transmission = np.sqrt(Int_Transmission)
# return Int_Reflectance, amp_reflectance, Int_Transmission, amp_transmission


# def PE_Lossy_Round_Trip_Coefficients(Int_Absorbtion):
# """
# Calculates the amplitude and power tranmission and absorbtion coefficients from the power absorbtion
# """
# amp_absorbtion = np.sqrt(Int_Absorbtion)
# Int_Transmission = 1 - Int_Absorbtion
# amp_transmission = np.sqrt(Int_Transmission)
# return Int_Absorbtion, amp_absorbtion, Int_Transmission, amp_transmission


# def PE_Intensity_Enhancement_LosslessMirror(Rin, Rout, Art):
# """
# Calculates the power/ intestity enhancement ratio circulating inside a cavity from the power reflectivies of the intput and output mirror (lossless) and the power absorbtion coefficient
# """
# Rin, rin, Tin, tin = PE_Lossless_Mirror_Coefficients(Rin)
# Rout, rout, Tout, tout = PE_Lossless_Mirror_Coefficients(Rout)
# I_Abs, amp_abs, I_Trans, amp_trans = PE_Lossy_Round_Trip_Coefficients(Art)
# Intensity_Enhancement_Ratio = tin ** 2 / (1 - rin * rout * amp_trans) ** 2

# totalloss1= 1-Rin*Rout*I_Trans
# totalloss2= 1-Rin +1-Rout +Art
# return Intensity_Enhancement_Ratio  # , totalloss1, totalloss2


# def PE_finesse(Rin, Rout, Art):
# """
# Calculates the finesse from the power reflectivies of the intput and output mirror (lossless) and the power absorbtion coefficient
# """
# Total_RT_loss = (1 - Rin) + (1 - Rout) + Art
# finesse = 2 * np.pi / (Total_RT_loss)
# return finesse
