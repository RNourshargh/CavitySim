from cavitysim.utils import Cavity, MirrorNormal, PathConstantIndex, LensThinVac


#"""THe following setup produces a 6mm beam diameter and is hopefully less scary"""
#cavity_elements_2 = [
#        mirror_normal(),
#        path_constant_index(0.4),
#        lens_thin_vac(0.15), #Edmund, query 785nm coated lenses
#        path_constant_index(0.1625),
#        lens_thin_vac(0.012), #Thorlabs lens
#        path_constant_index(0.11),
#        mirror_normal()
#]

"""THe following setup is reversed to see the small mode produces a 6mm beam diameter and is hopefully less scary"""
cavity_elements_2 = [
        mirror_normal(),
        path_constant_index(0.11),
        lens_thin_vac(0.012), #Thorlabs lens
        path_constant_index(0.1625),
        lens_thin_vac(0.15), #thorlabs V coated
        path_constant_index(0.4),
        mirror_normal()
]

GI3Cavity = cavity(cavity_elements_2, True)

m = GI3Cavity.ad()/2

EigenA = m + np.sqrt(m**2-1)
EigenB = m - np.sqrt(m**2-1)

print("EigenA:", EigenA)
print("EigenB", EigenB)

print(GI3Cavity.properties())
print(GI3Cavity.end_radius())


