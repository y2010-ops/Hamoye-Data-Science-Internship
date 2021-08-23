import pandas as pd
csv_df = pd.read_csv('X.csv')
csv_df.to_csv('X.csv', index=False)
print(csv_df)

#sometimes dependent on the xlrd library which can be installed by running pip install xlrd in the terminal

excel_df = pd.read_excel('About you (Responses).xlsx')
excel_df.to_excel('About you (Responses).xlsx')
print(excel_df)

#read table from a webpage and save as a dataframe

# html_df = pd.read_html()
# html_df.to_html()

url = 'https://github.com/WalePhenomenon/climate_change/blob/master/fuel_ferc1.csv?raw=true'
fuel_data = pd.read_csv(url, error_bad_lines= False)
fuel_data.describe(include='all')
print(fuel_data)

#check for missing values
print(fuel_data.isnull())
print(fuel_data.notnull())
print(fuel_data.isnull().sum())

#use groupby to count the sum of each unique value in the fuel unit column
print(fuel_data.groupby('fuel_unit')['fuel_unit'])
print(fuel_data.groupby('fuel_unit')['fuel_unit'].count())
fuel_data[['fuel_unit']] = fuel_data[['fuel_unit']].fillna(value='mcf')
print(fuel_data[['fuel_unit']])
print(fuel_data[['fuel_unit']].fillna(value='mcf').count())

#check if missing values have been filled
print(fuel_data.isnull().sum())
print(fuel_data.isnull().count())
print(fuel_data.groupby('report_year')['report_year', ].count())

# group by the fuel type code year and print the first entries in all the groups formed
print(fuel_data.groupby('fuel_type_code_pudl').first())
print(fuel_data.groupby('fuel_type_code_pudl').count())

fuel_df1 = fuel_data.iloc[0:19000].reset_index(drop=True)
fuel_df2 = fuel_data.iloc[19000:].reset_index(drop=True)
print(fuel_df1)
print(fuel_df2)

# check the length of both dataframes sum to the expected length
assert len(fuel_data) == (len(fuel_df1) + len(fuel_df2))
print(len(fuel_data))

# an inner merge will lose rows that do not match in both dataframes
pd.merge(fuel_df1, fuel_df2, how="inner")
print(pd.merge(fuel_df1, fuel_df2, how="inner"))

# outer Merge returns all rows in both dataframes
print(pd.merge(fuel_df1, fuel_df2, how="outer"))

# removes rows from the right dataframe that do not have a match with the left
# and keep all rows from the left
print(pd.merge(fuel_df1, fuel_df2, how="left"))


print(pd.concat([fuel_data]).reset_index(drop=True))
# check for duplicate rows
print(fuel_data.duplicated().any)















