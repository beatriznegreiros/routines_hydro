import numpy as np

# -------------------------------INPUT-------------------------------------------------------
number_of_river_patches = 44
id_file = 'mask_ul.dat'
outputfile = 'FA_ul-8_test.dat'
fraktion_file = 'fraktion8.csv'
schwelle_id = 999
schwelle_value = 1
# -------------------------------------------------------------------------------------------

# Import
id_array = np.genfromtxt(id_file, skip_header=8, dtype=np.float16, skip_footer=1)

# for fraction 8
section_fraction = np.append(np.genfromtxt(fraktion_file, skip_header=1, dtype=np.float16, delimiter=','),
                             schwelle_value)

# Defining sections
# Patch identifiers range from 10 till number of patches*10 plus the identifier for the schwellen (river ramps)
sections = np.append(np.array(range(10, (number_of_river_patches + 1) * 10, 10)), [schwelle_id], axis=0)  #include mask value for schwelle

print(sections)

if not np.shape(sections) == np.shape(section_fraction):
    print("Warning! Number of patches do not match")

for n, node in np.ndenumerate(id_array):
    for i, section in np.ndenumerate(sections):
        if node == section:
            id_array[n] = section_fraction[i]

np.savetxt(outputfile, id_array, fmt='%1.2f')


# for fraction 1:
'''section_fraction = np.array([0.25, 0.21, 0.17, 0.28, 0.18, 0.18, 0.2, 0.23, 0.19, 0.16, 0.19,
                             0.22, 0.13, 0.16, 0.19, 0.24, 0.29, 0.22, 0.16, 0.19, 0.22, 0.21,
                             0.2, 0.18,0.25,0.41,0.28,0.16,0.26,0.19,0.22,0.24,0.16,0.16,0.25,0.34,
                             0.29,0.23,0.21,0.17,0.25,0.32,0.3,0.27, 0.0])'''

# for the fraction 3:
'''section_fraction = np.array([0.41, 0.31, 0.21, 0.23, 0.18, 0.16, 0.20, 0.25, 0.20, 0.15,
                             0.24, 0.32, .07, 0.09, 0.11, 0.16, 0.21, 0.23, 0.25, 0.25,
                             0.25, 0.26, 0.27, 0.23, 0.28, 0.28, 0.23, 0.17, 0.14, 0.24,
                             0.18, 0.30, 0.17, 0.15, 0.18, 0.20, 0.23, 0.25, 0.24, 0.20,
                             0.25, 0.30, 0.25, 0.20, 0.0])'''

# for fraction 4
'''section_fraction = np.array([0.17,0.16,0.16,0.14,0.14,0.13,0.14,0.16,0.13,
                             0.1,0.14,0.18,0.67,0.38,0.1,0.12,0.15,0.17,0.19,
                             0.22,0.25,0.21,0.16,0.19,0.16,0.1,0.11,0.12,0.14,
                             0.15,0.16,0.13,0.25,0.2,0.18,0.17,0.19,0.21,0.21,0.18,
                             0.18,0.17,0.16,0.14,0.0])'''
# for the fraction 5:
'''section_fraction = np.array([0.07,0.14,0.21,0.19,0.19,0.13,0.15,0.17,0.2,0.22,0.18,0.14	,
                             0.1,0.18,0.26,0.22,0.18,0.24,0.3,0.23,0.17,0.17,0.17,0.31,0.19,
                             0.09,0.18,0.28,0.28,0.3,0.22,0.23,0.32,0.4,0.29,0.19,0.2,0.21,0.19,
                             0.28,0.21,0.14,0.18,0.21,0.0])'''

# for the fraction 6:
'''section_fraction = np.array([0.01	,0.03	,0.06	,0.08	,0.17	,0.2	,0.14	,0.08	,0.11	,0.14	,0.09	,0.05	,0.01	,0.1	,0.19	,0.12	,0.05	,0.03	,0.02	,0.02	,0.02	,0.04	,0.06	,0.02	,0.01	,0.02	,0.1	,0.17	,0.09	,0.06	,0.12	,0.01	,0.06	,0.04	,0.04	,0.03	,0.03	,0.03	,0.06	,0.11	,0.06	,0	,0.03	,0.06,  0.0])
'''

# for fraction 7:
'''section_fraction = np.array([0	,0.05	,0.1	,0.02	,0.09	,0.14	,0.09	,0.04	,0.1	,0.17	,0.09	,0.02	,0	,0.06	,0.12	,0.09	,0.06	,0.04	,0.03	,0.02	,0.02	,0.04	,0.06	,0.02	,0.02	,0.03	,0.04	,0.05	,0.03	,0.01	,0.03	,0.01	,0.03	,0.02	,0.01	,0.01	,0.02	,0.03	,0.01	,0.02	,0.01	,0	,0.01	,0.02 , 0.0])
'''