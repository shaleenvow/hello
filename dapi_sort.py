import pandas as pd

randomised_dict = {
    'Control 2': ['Plate_1_B2', 'Plate_1_D8', 'Plate_2_E5', 'Plate_2_F5'], 
    'Condition 8': ['Plate_1_B3', 'Plate_1_B7', 'Plate_1_G7', 'Plate_2_C6'], 
    'Condition 7': ['Plate_1_B4', 'Plate_1_E3', 'Plate_1_E11', 'Plate_2_G5'], 
    'Condition 15': ['Plate_1_B5', 'Plate_2_B7', 'Plate_2_D2', 'Plate_2_F9'], 
    'Condition 23': ['Plate_1_B6', 'Plate_1_D11', 'Plate_2_C3', 'Plate_2_F2'], 
    'Condition 25': ['Plate_1_B8', 'Plate_1_E9', 'Plate_1_F5', 'Plate_2_D5'], 
    'Condition 1': ['Plate_1_B9', 'Plate_1_D10', 'Plate_1_F6', 'Plate_2_D8'], 
    'Condition 20': ['Plate_1_B10', 'Plate_1_C7', 'Plate_2_B8', 'Plate_2_C4'], 
    'Condition 16': ['Plate_1_B11', 'Plate_1_G9', 'Plate_2_D4', 'Plate_2_E11'], 
    'Condition 13': ['Plate_1_C2', 'Plate_1_C9', 'Plate_2_C9', 'Plate_2_F4'], 
    'Condition 24': ['Plate_1_C3', 'Plate_1_F8', 'Plate_2_F11', 'Plate_2_G6'], 
    'Control 1': ['Plate_1_C4', 'Plate_1_F2', 'Plate_2_E8', 'Plate_2_G2'], 
    'Condition 2': ['Plate_1_C5', 'Plate_1_E8', 'Plate_1_G4', 'Plate_2_E9'], 
    'Condition 18': ['Plate_1_C6', 'Plate_1_F9', 'Plate_2_B4', 'Plate_2_B10'], 
    'Condition 11': ['Plate_1_C8', 'Plate_1_G2', 'Plate_2_E7', 'Plate_2_G8'], 
    'Condition 4': ['Plate_1_C10', 'Plate_1_E4', 'Plate_1_F10', 'Plate_2_G9'], 
    'Condition 19': ['Plate_1_C11', 'Plate_1_D4', 'Plate_2_B9', 'Plate_2_D9'], 
    'Control 4': ['Plate_1_D2', 'Plate_1_G8', 'Plate_2_B2', 'Plate_2_B11'], 
    'Condition 21': ['Plate_1_D3', 'Plate_1_F4', 'Plate_1_G3', 'Plate_2_B3'], 
    'Condition 6': ['Plate_1_D5', 'Plate_1_E2', 'Plate_2_E3', 'Plate_2_E4'], 
    'Condition 12': ['Plate_1_D6', 'Plate_2_B5', 'Plate_2_C5', 'Plate_2_G7'], 
    'Condition 14': ['Plate_1_D7', 'Plate_1_G11', 'Plate_2_C10', 'Plate_2_G10'], 
    'Condition 17': ['Plate_1_D9', 'Plate_1_G6', 'Plate_2_C2', 'Plate_2_D7'], 
    'Condition 10': ['Plate_1_E5', 'Plate_2_C11', 'Plate_2_D10', 'Plate_2_F7'], 
    'Condition 5': ['Plate_1_E6', 'Plate_2_D6', 'Plate_2_E10', 'Plate_2_G11'], 
    'Control 3': ['Plate_1_E7', 'Plate_1_F11', 'Plate_2_B6', 'Plate_2_D11'], 
    'Condition 26': ['Plate_1_E10', 'Plate_2_C8', 'Plate_2_D3', 'Plate_2_G3'], 
    'Condition 3': ['Plate_1_F3', 'Plate_1_G5', 'Plate_1_G10', 'Plate_2_E2'], 
    'Condition 22': ['Plate_1_F7', 'Plate_2_C7', 'Plate_2_F6', 'Plate_2_G4'], 
    'Condition 9': ['Plate_2_E6', 'Plate_2_F3', 'Plate_2_F8', 'Plate_2_F10']}

# Reading the macro .csv files and isolating count and plate names
df_plate_1 = pd.read_csv(r"C:\Users\shale\hello\csv\Summary_DAPI_9426.csv")
df_plate_2 = pd.read_csv(r"C:\Users\shale\hello\csv\Summary_DAPI_9427.csv")
total_counts = [i for i in df_plate_1["Count"]] + [i for i in df_plate_2["Count"]]
plate_1_well_info_raw = [f"Plate_1_" + i[16:19] for i in df_plate_1["Slice"]] # Isolating plate well info from macro .csv and storing into a string: "Plate_1_B2_"'

# Removes any underscores at the end of any plate and well info: "Plate_1_B2"
plate_1_well_info = []
for i in plate_1_well_info_raw: 
    if i[10] == "_":
        plate_1_well_info.append(i.rstrip(i[-1]))
    else: plate_1_well_info.append(i)

plate_well_info = plate_1_well_info + [i.replace("Plate_1", "Plate_2") for i in plate_1_well_info] # Generates a final master list of Plate 1 and Plate 2 wells

plate_well_dapi_dict = dict()

for idx, well in enumerate(plate_well_info): # Generates a dictionary of the plate/well info and the corresponding DAPI count (i.e. Plate_1_B2: 883)
        plate_well_dapi_dict[well] = total_counts[idx]

final_dict = dict()

randomised_condition_list = [i for i in randomised_dict.keys()] # Takes the keys of the master dict and stores in a list to iterate over in subsequent lines

for idx, condition in enumerate(randomised_condition_list):
    master_list = []
    for quartet in list(randomised_dict.values()): # Iterates over a list of a quartet list of the plate well destinations [[Plate_1_E6, Plate_2_F3, Plate_2_F8, Plate_2_F10], [Plate_1_G10, Plate_2_E2 ]
        sublist = []
        for each_plate_well in quartet:
            sublist.append(plate_well_dapi_dict[each_plate_well]) # Uses in each set of four replicate destinations as keys to obtain the Count (value) 
        master_list.append(sublist) # Appends the list of quartet of counts [1,2,3,4] to a master list e.g. [[1,2,3,4], [3,5,7,9], ...]
    final_dict[condition] = master_list[idx] # Generates a new final dictionary {"Condition X": [2345, 4353, 5645, 5464] <-- These are DAPI counts}

print(plate_well_dapi_dict)
# df = pd.DataFrame(final_dict)
# df.to_csv("output.csv")

