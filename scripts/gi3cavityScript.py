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

#
#cavity_elements_2 = [
#        mirror_normal(),
#        path_constant_index(0.4),
#        lens_thin_vac(0.1),
#        path_constant_index(0.128),
#        lens_thin_vac(0.025), #Thorlabs lens
#        path_constant_index(0.06),
#        mirror_normal()
#]

cavity_elements_2 = [
        mirror_normal(),
        path_constant_index(0.1936),
        lens_thin_vac(0.1),
        path_constant_index(0.0814),
        lens_thin_vac(-0.02), #Thorlabs lens
        path_constant_index(0.05),
        mirror_normal()
]




Con25Con100 = cavity(cavity_elements_2, True)

print(Con25Con100.end_radius())