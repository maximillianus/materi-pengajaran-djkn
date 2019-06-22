# List

#############################################
############### Creating List ###############
#############################################
# How to create a list?
number_list = [1, 2, 3, 4, 5]
print('my_integer_list:', number_list)


list_of_building_types = ['mall', 'gudang', 'ruko', 'rumah' ,'hotel', 'apartemen']
print('my_building_list:', list_of_building_types)


#############################################
########### subset list element  ############
#############################################
# How to pick element from list?

# select 1st element
# list is started from 0
first_building_type = list_of_building_types[0]
print('first_building:', first_building_type)

# to  select last element:
last_number = number_list[-1]
second_last_number = number_list[-2]
print('last_number:', last_number)
print('second_last_number:', second_last_number)

# list ends with 4 since it begins with 0
last_number = number_list[4]
print('last_number:', last_number)

# Select multiple list element:
list_of_building_types = ['mall', 'gudang', 'ruko', 'rumah' ,'hotel', 'apartemen']
two_building_types = list_of_building_types[1:3]
print('two_buildings:', two_building_types)

#############################################
######## list from a range of number ########
#############################################
# Generate a number into list
# list_from_range = list(range(1,10))
# print('list_from_range:', list_from_range)


#############################################
################ list length ################
#############################################
# # Check length of list
print('length of list:', len(list_of_building_types) )