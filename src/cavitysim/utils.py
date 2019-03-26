import numpy as np




def path_free_space(path_length, n0):
    """
    Zeb's example. Careful Doesn't really work
    """
    abcd = np.array([[1, path_length], [0, 1]])
    opl = path_length*n0

    return abcd, opl

def rayleigh_range_w0(w0):
    """
    Calculate Rayleigh Range from waist w0
    """
    zr = np.pi*w0**2/wavelength
    return zr

def radius_from_q(q):
    """
    Calculates the beam radius w from q the complex beam parameter at the point q is definied
    """
    return np.sqrt(-wavelength/(np.pi*np.imag(1/q)))

def lens_thin_vacuum_abcd(f):
    """
    Generates abcd matrix, for thin lens, focal length f (metres)
    """
    abcd = np.matrix([[1,0],[-1/f , 1]])
    opl = 0 #By definition for a thin lens
    return abcd, opl

def mirror_planar_normal():
    """
    Generates abcd matrix, for planar mirror at normal insidence
    """
    abcd = np.matrix([[1,0],[0, 1]])
    opl = 0 #By definition for a planar mirror
    return abcd, opl

def abcd_stability(abcd):
    """
    Tests stability of a cavity defined by an abcd matrix.
    """
    AD = np.trace(abcd)
    if (AD<=2) and (AD>=-2):
        print("Cavity is stable")
        print("A+D = " +str(AD))
        CavStab = True
    elif (AD>2) or (AD<-2):
        print("Cavity is unstable")
        print("A+D = " +str(AD))
        CavStab = False
    else:
        print("Error:Invalid abcd matrix")
    return AD, CavStab
        

wavelength = 780E-9