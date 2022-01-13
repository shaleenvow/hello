from opentrons import protocol_api
from opentrons.commands.commands import drop_tip, pick_up_tip

# This OT2 protocol dispenses each of the 30 conditions/controls into random locations across 2 x 96 well plates as per a randomised dictionary

metadata = {
    'protocolName': 'OT2 Plate Randomisation',
    'author': 'Name <shaleen@vowfood.com>',
    'description': 'Protocol to randomise conditions',
    'apiLevel': '2.9'
}

randomised_dict = { # A randomised dictionary consisting of conditions/controls and their respective destinations across 2 x 96 well plates
    'Control 2': ['Plate_1_B2', 'Plate_1_D8', 'Plate_2_E5', 'Plate_2_F5'], 
    'Condition 8': ['Plate_1_B3', 'Plate_1_B7', 'Plate_1_G7', 'Plate_2_C6'], 
    'Condition 7': ['Plate_1_B4', 'Plate_1_E3', 'Plate_1_E11', 'Plate_2_G5'], 
    'Condition 15': ['Plate_1_B5', 'Plate_2_B7', 'Plate_2_D2', 'Plate_2_F9'], 
    'Condition 23': ['Plate_1_B6', 'Plate_1_D11', 'Plate_2_C3', 'Plate_2_F2'], 
    'Condition 25': ['Plate_1_B8', 'Plate_1_E9', 'Plate_1_F5', 'Pl ate_2_D5'], 
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

DSD_MEDIA_VOLUME = 1500 # The volume of media to be added to each well of the 96 2.4mL deep well plate (Note: specify volume per replicate, e.g. 1500uL x 4 replicates = 6mL total)

# PROTOCOL START        
def run(protocol: protocol_api.ProtocolContext):

    # P1000 FUNCTIONS:
    # Transfer function: defines the function of the P1000 aspirating each Control/Condition from tubes and dispensing in wells.
    def p1000_transfer_function(media_volume, tube_rack, tube, plate, plate_well):
        p1000.flow_rate.aspirate = 600
        p1000.flow_rate.dispense = 600
        p1000.transfer(media_volume, tube_rack.wells()[tube], plate.wells_by_name()[plate_well].top(), new_tip= "never")


    # Loading pipette, labware, plates:
    p1000_tiprack_1 = protocol.load_labware("opentrons_96_tiprack_1000ul", "11")
    p1000 = protocol.load_instrument("p1000_single", "left", tip_racks=[p1000_tiprack_1])
    tube_rack_1 = protocol.load_labware("opentrons_15_tuberack_falcon_15ml_conical", "8")
    tube_rack_2 = protocol.load_labware("opentrons_15_tuberack_falcon_15ml_conical", "9")
    Plate_1 = protocol.load_labware("usascientific_96_wellplate_2.4ml_deep", "5")
    Plate_2 = protocol.load_labware("usascientific_96_wellplate_2.4ml_deep", "6")

    # Filtering the randomised dictionary given above into a "Conditions" dictionary and "Controls" dictionary:
    conditions_dict = dict()
    controls_dict = dict()

    for (key,value) in randomised_dict.items():
        if "Condition" in key:
            conditions_dict[key] = value
    
    for (key,value) in randomised_dict.items():
        if "Control" in key:
            controls_dict[key] = value
    
    # Numerically sorting the condition and control numbers in ascending order:
    conditions = list(conditions_dict.keys()) # Conditions = ["Condition 1", "Condition 2", "Condition 16" ...]
    controls = list(controls_dict.keys()) 
    sorted_conditions = sorted(conditions, key=lambda x: int(x[10:12])) # Sorts the above conditions list by ascending condition number
    sorted_controls = sorted(controls, key=lambda x: int(x[8]))
    
    # Isolating the index (idx) of each sorted Condition as the "from" and isolating the destination info (Plate and Well) as the "to"
    # Then the P1000 transfer function is called and the isolated index, plate and well information are used as the arguments.
    for idx, curr_condition in enumerate(sorted_conditions):
       curr_well_destinations_raw = conditions_dict[curr_condition] # ['Plate_1_B9', 'Plate_1_D10', 'Plate_1_F6', 'Plate_2_D8']
       curr_plate_destinations = [i[0:7] for i in curr_well_destinations_raw] # Isolates the plate destinations i.e. ['Plate_1', 'Plate_1', 'Plate_1', 'Plate_2']
       curr_well_destinations = [i[8:10] for i in curr_well_destinations_raw] # Isolates the well destinations i.e. ['B9', 'D1', 'F6', 'D8']
    
    # OT2 iterates through condition plate and well destinations 
       p1000.pick_up_tip()
       for each_plate, each_well in zip(curr_plate_destinations,curr_well_destinations):
           if each_plate == "Plate_1":
              each_plate = Plate_1
           else: each_plate = Plate_2
        
           if idx < 15:
               p1000_transfer_function(DSD_MEDIA_VOLUME, tube_rack_1, idx, each_plate, each_well)
           else: p1000_transfer_function(DSD_MEDIA_VOLUME, tube_rack_2, idx - 15, each_plate, each_well)
       p1000.drop_tip()
    
    # The same information is isolated for the Controls and the P1000 transfer is called.
    for idx, curr_control in enumerate(sorted_controls):
        curr_cntrl_well_destinations_raw = controls_dict[curr_control]
        curr_cntrl_plate_destinations = [i[0:7] for i in curr_cntrl_well_destinations_raw] # Isolates the plate destinations i.e. ['Plate_1', 'Plate_1', 'Plate_1', 'Plate_2']
        curr_cntrl_well_destinations = [i[8:10] for i in curr_cntrl_well_destinations_raw] # Isolates the well destinations i.e. ['B9', 'D1', 'F6', 'D8']
    
    # OT2 iterates through control plate and well destinations 
        p1000.pick_up_tip()
        for each_plate, each_well in zip(curr_cntrl_plate_destinations,curr_cntrl_well_destinations):
           if each_plate == "Plate_1":
              each_plate = Plate_1
           else: each_plate = Plate_2
           p1000_transfer_function(DSD_MEDIA_VOLUME, tube_rack_2, idx + 11, each_plate, each_well)
        p1000.drop_tip()
