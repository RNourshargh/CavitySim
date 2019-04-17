from cavitysim.utils import cavity, mirror_normal, path_constant_index, lens_thin_vac

#cavity_elements_1 = [
#        mirror_normal(),
#        path_constant_index(),
#        lens_thin_vac(),
#        path_constant_index(),
#        lens_thin_vac(0.1), #Thorlabs lens
#        path_constant_index(0.4),
#        mirror_normal()
#        ]

#"""THe following setup produces a 6mm beam diameter"""
#cavity_elements_2 = [
#        mirror_normal(),
#        path_constant_index(0.4),
#        lens_thin_vac(0.1),
#        path_constant_index(0.1077),
#        lens_thin_vac(0.0075), #Thorlabs lens
#        path_constant_index(0.11),
#        mirror_normal()
#]
#"""THe following setup produces a 6mm beam diameter and is hopefully less scary"""
#cavity_elements_2 = [
#        mirror_normal(),
#        path_constant_index(0.4),
#        lens_thin_vac(0.2),
#        path_constant_index(0.2165),
#        lens_thin_vac(0.015), #Thorlabs lens
#        path_constant_index(0.11),
#        mirror_normal()
#]


"""THe following setup produces a 6mm beam diameter and is hopefully less scary"""
cavity_elements_2 = [
        mirror_normal(),
        path_constant_index(0.4),
        lens_thin_vac(0.15), #Edmund, query 785nm coated lenses
        path_constant_index(0.1628),
        lens_thin_vac(0.0125), #Thorlabs lens
        path_constant_index(0.11),
        mirror_normal()
]






Con25Con100 = cavity(cavity_elements_2, True)
print(Con25Con100.properties())
print(Con25Con100.end_radius())