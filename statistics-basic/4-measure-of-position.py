import pandas as pd

#########################
####### READ FILE #######
#########################

films = pd.read_csv('./film-outliers.csv')


# Quantile 95
qt95 = films.Length.quantile(0.95)
print('95% of films has duration less than:', qt95, 'min')

# Quantile 99
qt99 = films.Length.quantile(0.99)
print('99% of films has duration less than:', qt99, 'min')
