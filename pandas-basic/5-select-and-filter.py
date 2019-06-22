import pandas as pd

#########################
####### READ FILE #######
#########################

films = pd.read_csv('../statistics-basic/film.csv')

# Select
# ge = greater or equal than ( >= )
print(films[films.Length.ge(100.0)].head())

# lt = less than ( < )
print(films[films.Length.lt(60.0)].head())

# Filter
long_films = films[films.Length.ge(120)].copy()
print(long_films.head())

# le = less or equal than
short_films = films[films.Length.le(40)].copy()
print(short_films.head())


samurai_film = films[films.Title.str.contains(' war', case=False)]
print(samurai_film)