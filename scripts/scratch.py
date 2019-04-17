from cavitysim.utils import cavity, mirror_normal, path_constant_index, lens_thin_vac

CAVITY_SETUP = [
    mirror_normal(5),
    path_constant_index(0.40756),
    mirror_normal()
]

excav = cavity(CAVITY_SETUP, True)

print("Cavity setup: {}".format(CAVITY_SETUP))

print("ABCD is: {}".format(excav.abcd()))
print("AD is: {}".format(excav.ad()))
excav.properties()
print(excav.end_radius())
print(excav.ad()/2)

#"""Run the cavity script for the cavity I have already built"""
#Con50Con100 = cavity(
#    [
#        mirror_normal(),
#        path_constant_index(0.14),
#        lens_thin_vac(0.05),
#        path_constant_index(0.17),
#        lens_thin_vac(0.1),
#        path_constant_index(0.2),
#        mirror_normal()
#    ],
#    True
#)
#
#print("")
#print("Con50Con100 properties")
#print("ABCD is: {}".format(Con50Con100.abcd()))
#print("AD is: {}".format(Con50Con100.ad()))
#Con50Con100.properties()
