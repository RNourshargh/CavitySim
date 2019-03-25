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
    
wavelength = 780E-9    
	
print(rayleigh_range_w0(500E-6))


