import numpy as np

# -------------------------------INPUT-------------------------------------------------------
number_of_river_patches = 44
id_file = 'id_mesh_refined_acuna.dat'
outputfile = 'dzg_2007_acuna_option_1.dat'
schwelle_id = 999
schwelle_value = 0
value_bed = 3
value_banks = 0
# -------------------------------------------------------------------------------------------

usecols = np.arange(2, 46)
# Import
id_array = np.genfromtxt(id_file, skip_header=8, dtype=np.float16, skip_footer=1)


# Defining sections
# Patch identifiers range from 10 till number of patches*10 plus the identifier for the schwellen (river ramps)
sections_bed = np.arange(10, (number_of_river_patches + 1) * 10, 10)
                      #include mask value for schwelle


sections_banks = np.arange(11, (number_of_river_patches + 1) * 10, 10)


for i, section in np.ndenumerate(sections_bed):
    id_array = np.where(id_array != section, id_array, value_bed)

for i, section in np.ndenumerate(sections_banks):
    id_array = np.where(id_array != section, id_array, value_banks)

    id_array = np.where(id_array != schwelle_id, id_array, schwelle_value)


np.savetxt(outputfile, id_array, fmt='%1.2f')