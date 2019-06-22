import pandas as pd

#########################
####### READ FILE #######
#########################

countries = pd.read_excel('./countries-continent-excel.xlsx', 
    sheet_name='countries')
print(countries.head(7) )
print()


# #########################
# ######### COUNT #########
# #########################

# Which continent has the most countries?
count_of_countries = countries.Continent.value_counts()
print(count_of_countries)
print()

# #########################
# ####### Percentage #######
# #########################

# # Which continent has the most countries? In percentage
count_of_countries = countries.Continent.value_counts(normalize=False)
print(count_of_countries)


