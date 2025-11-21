import pandas as pd

data = {'floor': [1, 2, 2, 3, 1, 1, 4, 2]}
df = pd.DataFrame(data)

floor_counts_df = df['floor'].value_counts().to_frame()
print(floor_counts_df)