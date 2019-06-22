import pandas as pd

############################################
##### Creating dataframe from scratch ######
############################################

df_from_scratch = pd.DataFrame({
    'x': ['baju', 'makan', 'rumah'],
    'y': ['sandang', 'pangan', 'papan'],
    'z': [0,1,2]

    })

print(df_from_scratch)
print()

############################################
###### Creating dataframe from file ########
############################################

df = pd.read_csv('../statistics-basic/mean-vs-median.csv')
print(df.head())
