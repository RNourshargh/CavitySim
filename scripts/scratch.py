from cavitysim.utils import cavity, mirror_normal, path_constant_index

CAVITY_SETUP = [
    mirror_normal(0.2),
    path_constant_index(0.1),
    mirror_normal(0.2)
]

excav = cavity(CAVITY_SETUP, True)

print("Cavity setup: {}".format(CAVITY_SETUP))

print("ABCD is: {}".format(excav.abcd()))
print("AD is: {}".format(excav.ad()))
excav.properties()

"""Run the cavity script for the cavity I have already built"""
#Con50Con100 = cavity([mirror_normal(),path_constant_index(0.14),lens_thin_vac(0.05),path_constant_index(0.17),lens_thin_vac(0.1),path_constant_index(0.2),mirror_normal()],True)
