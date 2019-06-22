import pandas as pd

#########################
####### READ FILE #######
#########################

df = pd.read_csv('./mean-vs-median.csv')
print(df)


### Mean, Median, Standard Deviation for normal data: ##
normal_data_mean = df.normal_data.mean()
normal_data_median = df.normal_data.median()
normal_data_std = df.normal_data.std()

print('normal_data_mean:', normal_data_mean)
print('normal_data_median:', normal_data_median)
print('normal_data_std:', normal_data_std)

print('\n##########################\n')

### Mean, Median, Standard Deviation for outlier data: ##
outlier_data_mean = df.outlier_data.mean()
outlier_data_median = df.outlier_data.median()
outlier_data_std = df.outlier_data.std()

print('outlier_data_mean:', outlier_data_mean)
print('outlier_data_median:', outlier_data_median)
print('outlier_data_std:', outlier_data_std)


