# Conditional Statement

list_of_building_types = ['mall', 'gudang', 'ruko', 'rumah' ,'hotel', 'apartemen']

list_of_personal_building = []
list_of_business_building = []

for building in list_of_building_types:
    if building == 'ruko' or building == 'rumah':
        list_of_personal_building.append(building)
    else:
        list_of_business_building.append(building)

print('List of personal building:', list_of_personal_building)
print('List of business building:', list_of_business_building)