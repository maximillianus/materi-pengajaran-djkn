import pandas as pd

#########################
####### READ FILE #######
#########################

films = pd.read_csv('./film.csv')

films = films.dropna()
print(films.info())

print(films.head())
# print()


#########################
######### Mean #########
#########################

# What is the average duration of the movies?
film_length_mean = films.Length.mean()
print('Average of films length:' ,film_length_mean)
print()

#########################
######### Median ######## 
#########################

# What is the median duration length of the movie?
film_length_median = films.Length.median()
print('Median of films length:' ,film_length_median)
print()

#########################
######### Mode ######## 
#########################

# Which year has the most produced films?
most_active_year = films.Year.value_counts()[:10]
print(most_active_year)
