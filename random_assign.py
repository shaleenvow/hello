import random
from typing import final

numbers = [x for x in (range(2,12))]
letters = ["B","C","D","E","F","G"]
plate_1 = ["Plate_1" + "_" + letter + str(number) for letter in letters for number in numbers]
plate_2 = ["Plate_2" + "_" + letter + str(number) for letter in letters for number in numbers]
total_wells = tuple(plate_1 + plate_2)

number_of_conditions = random.sample(range(1,27),26)
replicate_condition_list = [number_of_conditions for replicate in range(4)]
conditions = ["Condition" + " " + str(item) for sublist in replicate_condition_list for item in sublist]

number_of_controls = random.sample(range(1,5),4)
replicate_control_list = [number_of_controls for replicate in range(4)]
controls = ["Control" + " " + str(item) for sublist in replicate_control_list for item in sublist]

controls_with_conditions = controls + conditions
random.shuffle(controls_with_conditions)
print(controls_with_conditions)

final_dict = dict()

for i in range(len(controls_with_conditions)):
    current_well =  total_wells[i]
    current_condition = controls_with_conditions[i]

    if current_condition in final_dict:
        final_dict[current_condition].append(current_well)
    else:
        final_dict[current_condition] = []
        final_dict[current_condition].append(current_well)

print(final_dict)


