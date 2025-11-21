import pandas as pd

df = pd.read_csv('your_dataset.csv')
df.drop(['id', 'Unnamed: 0'], axis=1, inplace=True)
print(df.describe())
