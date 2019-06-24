from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac

CAVITY_SETUP = [
    MirrorNormal(5),
    PathConstantIndex(0.40756),
    MirrorNormal()
]

excav = Cavity(CAVITY_SETUP, True)

print("Cavity setup: {}".format(CAVITY_SETUP))

print("Cavity elements: {}".format(excav.elements))

print("ABCD is: {}".format(excav.abcd()))
print("AD is: {}".format(excav.ad()))
excav.properties()
print(excav.end_radius())
print(excav.ad()/2)