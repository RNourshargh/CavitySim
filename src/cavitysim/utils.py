import numpy as np
#from abc import ABCMeta, abstractmethod
import copy


class cavity(object):
    """An optical resonator.

    Attributes:
        elements: a list of optical elements (class objects) defining the cavity
        linear: Boolean to indicate if the cavity is linear or standing wave. (Linear cavities must be defined from an end mirror)
        n0: Refractive index of free space, default=1
    """
    
    
    def __init__(self,input_elements,linear,n0=1):
        self.input_elements = input_elements
        self.linear = linear
        self.n0 = n0
        self.unfolded = False
        self.elements = copy.deepcopy(input_elements)
        self.unfold()
        
        
    def unfold(self):
        """Unfold linear cavities"""
        if self.linear == True and self.unfolded == False:#Check the cavity is linear and hasn't been unfolded
            self.returntrip = self.elements[1:-1] #Slice off the end mirrors
            self.returntrip.reverse() #reverse order of optical elements for the return trip
            self.elements.extend(self.returntrip) #Add the reverse trip optics to the elements list
            self.unfolded = True    #Record that the cavity has been unforlded
        else:
            self.unfolded = True    
        
    def abcd(self):
        """Generates the abcd matrix for the cavity, Be cautious in linear cavities with thick lenses"""

        self.elements_abcd_list = [] #Initialise list of abcd matrices
        for element in self.elements:
            #print(element)
            #print(element.abcd())
            self.elements_abcd_list.append(element.abcd()) #populate list of abcd matrices
            
        abcd_matrix = np.matrix([[1,0],[0,1]]) #Initialise cavity abcd matrix
        
        for matrix in self.elements_abcd_list:
            abcd_matrix = np.matmul(abcd_matrix,matrix) #multiply element abcd matrices together
            
        return abcd_matrix
            

class lens_thin_vac(object):
    """A thin lens in a vacuum
    
    Attributes:
        f: focal length (metres)
    """
    
    def __init__(self, f):
        self.f = f
        
    def abcd(self):
        """Generate the abcd matrix for the thin lens"""
        return np.matrix([[1,0],[-1/(self.f) , 1]])
    
    def opl(self):
        """Calculate the optical path length for the thin lens"""
        return 0
    
class path_constant_index(object):
    """Propagation through a path of refractive index n
    
    Attributes:
        d: path length (metres)
        n: refractive index, default n=1
    """
    
    def __init__(self,d,n=1):
        self.d = d
        self.n = n
        
    def abcd(self):
        """Returns the abcd matrix for the propagation"""
        return np.matrix([[1,self.d],[0 , 1]])

    def opl(self):
        """Returns the optical path length for this propagation"""
        return self.d*self.n
    
class mirror_normal(object):
    """Reflection from a mirro of ROC R, (R>0 for concave mirrors)
    
    Attributes:
        roc: Radius of curvature (metres), Default infinite (planar mirror)
        
    """
    def __init__(self, roc=np.inf):
        self.roc =roc
    
    def abcd(self):
        """Returns abcd matrix for reflection from this mirror"""
        return np.array([[1,0],[-2/self.roc , 1]])
    def opl(self):
        """returns the optical path length for reflection, 0"""
        return 0
    


def legacy_path_constant_index(path_length, n0):
    """
    generate the abcd matrix for propagation in a medium of constant refractive index
    """
    abcd = np.array([[1, path_length], [0, 1]])
    opl = n0*path_length
    return abcd , opl

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

def legacy_lens_thin_vacuum_abcd(f):
    """
    Generates abcd matrix, for thin lens, focal length f (metres)
    """
    abcd = np.matrix([[1,0],[-1/f , 1]])
    opl = 0 #By definition for a thin lens
    return abcd, opl

def legacy_mirror_planar_normal():
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
    else:
        print("Cavity is unstable")
        print("A+D = " +str(AD))
        CavStab = False
    return AD, CavStab


wavelength = 780E-9