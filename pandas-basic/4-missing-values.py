import pandas as pd

#########################
####### READ FILE #######
#########################

films = pd.read_csv('../statistics-basic/film.csv')

##################################
# Check how many missing values
##################################

print(films[films.Length.isnull()].head())


# How many missing value for column Length?
missing_value_for_length = films['Length'].isnull().sum()
print('missing value for film duration:', missing_value_for_length)

# How many missing value for EVERY columns?
for col in films.columns:
    missing_value = films[col].isnull().sum()
    print('Missing value for', col, ' is:', missing_value)


#########################
# DROP missing Values
#########################

films_with_missing_values_dropped = films.dropna()


##################################
# FILL missing Values (Imputation)
##################################

length_mean = films.Length.mean()
films_imputation = films.Length.fillna(length_mean)


