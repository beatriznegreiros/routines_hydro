# routines_hydro
Useful routines for handling input and output data from HYDRO_AS-2D and HYDRO_FT-2D

The following routines are included:
- ``fill_fractions_al.py``: This routine produces input files containing the sediment fractions of the active layer. It uses an `id_file`, which contains id numbers of each river section, to fill the respective sediment fraction of that river section. 
- ``fil_fractions_ul_py``: This routine does the exact same as ``fill_fractions_al.py`` but for the underlayer.
- ``fill_dzg``: This routines produces input files containing the erodibility factor of each river section. 

### fill_fractions_al.py and fill_fractions_ul.py

*Please note:   the id of river banks are delimited by multiples of 10 (ex.: 10,20,30...)
                the id of the river beds are delimited by (multiples of 10) + 1 (ex.: 11,21,31..)*
The routine takes the following input parameters:
- ``number_of_river_patches``: integer, number of sections (i.e., patches) with which the river was discretized. In the present case we have 44 sections.
- ``outputfile``: string, path of the output file being generated.
- ``fraktion_file``: string, path of the file used to take the respective fraction. If this file is changed the position of the rows and columns have to be maintained!! (i.e., only values should be changed).
- ``schwelle_id``: integer, *id* value used to indicate that a is node included in a river ramp (Schwelle).
- ``schwelle_value``: float, value of the fraction for the schwelle.
- ``frak``: integer, number of the fraction (fractions: 1,2,3,4,5,6,7,8).

        

### fill_dzg.py

*Please note:   the id of river banks are delimited by multiples of 10 (ex.: 10,20,30...)
                the id of the river beds are delimited by (multiples of 10) + 1 (ex.: 11,21,31..)*
The routine takes the following input parameters:
- ``number_of_river_patches``: integer, number of sections (i.e., patches) with which the river was discretized. In the present case we have 44 sections.
- ``outputfile``: string, path of the output file being generated.
- ``schwelle_id``: integer, *id* value used to indicate that a is node included in a river ramp (Schwelle).
- ``schwelle_value``: float, value of the fraction for the schwelle.
- ``value_bed``: float, the value of the erodibility factor for the river bed.
- ``value_banks``: float, the value of the erodibility factor for the river bank.

## Dependency
- numpy 

