"""
Binding Energy Per Nucleon
--------------------------

This is the Python file for generating the graph as specified on Pg. 300 on
*Physics HL (Second Edition)* By Chris Hampton, Pearson.
"""

from matplotlib import pyplot as plt

element_symobols = ('H', 'D', 'He', 'Li', 'Be', 'N', 'Cl', 'Fe', 'Ni', 'Kr', 'Sr', 'Ba', 'Pb', 'Rn', 'Ra', 'U')
atomic_numbers = (1, 1, 2, 3, 4, 7, 17, 26, 28, 36, 38, 56, 82, 86, 88, 92)
number_of_nucleons = (1, 2, 3, 6, 9, 14, 35, 54, 58, 78, 84, 130, 204, 211, 223, 233)
masses_u = (1.0078, 2.0141, 3.0160, 6.0151, 9.0122, 14.0031, 34.9689, 53.9396, 57.9353, 77.9204, 83.9134, 129.9063, 203.9730, 210.9906, 223.0185, 233.0396)
neutron_mass = 1.00866
hydrogen_mass = 1.00782

binding_energy_per_nucleon = []
for i in range(len(atomic_numbers)):
    supposed_mass_u = atomic_numbers[i] * hydrogen_mass + (number_of_nucleons[i] - atomic_numbers[i]) * neutron_mass
    mass_defect_u = supposed_mass_u - masses_u[i]
    energy_released_mev = mass_defect_u * 931.5
    binding_energy_per_nucleon.append(energy_released_mev / number_of_nucleons[i])

plt.title('Binding Energy per Nucleon')
plt.plot(number_of_nucleons, binding_energy_per_nucleon, marker='o')
for i, label in enumerate(element_symobols):
    plt.annotate(label, (number_of_nucleons[i], binding_energy_per_nucleon[i]))
plt.show()
