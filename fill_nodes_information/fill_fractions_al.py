import numpy as np

# -------------------------------INPUT-------------------------------------------------------
number_of_river_patches = 44
id_file = 'id_mesh_refined_acuna.dat'
outputfile = '03_refined_mesh_by_acuna/FA_al-8.dat'
fraktion_file = 'Korngroeßenverteilung_Mesh_final_new.csv'
schwelle_id = 999
schwelle_value = 1
frak = 8
# -------------------------------------------------------------------------------------------

usecols = np.arange(2, 46)

# Import
id_array = np.genfromtxt(id_file, skip_header=8, dtype=np.float16, skip_footer=1)

# Read the fractions for each section according to the fraktion_file given path
section_fraction_bed = np.append(np.genfromtxt(fraktion_file, max_rows=1, skip_header=10-frak, usecols=usecols, dtype=np.float16, delimiter=','),
                             schwelle_value)


section_fraction_banks = np.append(np.genfromtxt(fraktion_file, max_rows=1, skip_header=24-frak, usecols=usecols, dtype=np.float16, delimiter=','),
                             schwelle_value)

# Defining sections
# Patch identifiers range from 10 till number of patches*10 plus the identifier for the schwellen (river ramps)
sections_bed = np.append(np.arange(10, (number_of_river_patches + 1) * 10, 10), [schwelle_id], axis=0)
                      #include mask value for schwelle


sections_banks = np.append(np.arange(11, (number_of_river_patches + 1) * 10, 10), [schwelle_id], axis=0)


if not np.shape(sections_bed) == np.shape(section_fraction_bed) and np.shape(sections_bed) == np.shape(section_fraction_banks):
    print("Warning! Number of patches do not match")

if frak == 8:
    id_array = np.where(id_array != 0, id_array, 1)

for i, section in np.ndenumerate(sections_bed):
    id_array = np.where(id_array != section, id_array, section_fraction_bed[i])

for i, section in np.ndenumerate(sections_banks):
    id_array = np.where(id_array != section, id_array, section_fraction_banks[i])

# for filling fraction 8:


np.savetxt(outputfile, id_array, fmt='%1.2f')