from cavitysim.utils import cavity, mirror_normal, path_constant_index, lens_thin_vac


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





Con25Con100 = cavity(cavity_elements_2, True)
print(Con25Con100.properties())
print(Con25Con100.end_radius())