import pandas as pd

#########################
####### READ FILE #######
#########################

films = pd.read_csv('./film-outliers.csv')

# Clear rows which has empty value
films = films.dropna()

###################################
####### 5 number statistics #######
###################################

print('5 Number statistics')
print(films.describe())
print()

###################################
############# RANGE ###############
###################################

max_duration_length = films.Length.max()
min_duration_length = films.Length.min()
print('Range of films duration:', min_duration_length, '-', max_duration_length)
print()

###################################
####### Interquartile Range #######
###################################

q1 = films.Length.quantile(0.25)
q3 = films.Length.quantile(0.75)
iqr = q3 - q1
print('Q1:', q1)
print('Q3:', q3)
print()

###################################
############ Outlier ##############
###################################

# How many films with abnormal duration?
lower_bound_mild = q1 - (1.5 * iqr)
upper_bound_mild = q3 + (1.5 * iqr)
lower_bound_extreme = q1 - (3.0 * iqr)
upper_bound_extreme = q3 + (3.0 * iqr)

filter_mild_outlier = films.Length.lt(lower_bound_mild) | films.Length.gt(upper_bound_mild)
filter_extreme_outlier = films.Length.lt(lower_bound_extreme) | films.Length.gt(upper_bound_extreme)
films_with_abnormal_duration = films[filter_mild_outlier]
films_with_very_abnormal_duration = films[filter_extreme_outlier]
print('How many films with abnormal duration?',len(films_with_abnormal_duration))
print('How many films with very abnormal duration?', len(films_with_very_abnormal_duration))
print()

# Is 66 abnormal & 26 abnormal movies a lot?
print('Percentage of abnormal movies:' , len(films_with_abnormal_duration) * 100.0 / len(films))
print('Percentage of very abnormal movies:' , len(films_with_very_abnormal_duration) * 100.0 / len(films))

print(films_with_very_abnormal_duration)
