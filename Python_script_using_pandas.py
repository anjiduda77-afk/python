import pandas as pd

data = {'floor': [1, 2, 2, 3, 1], 'price': [100000, 150000, 120000, 130000, 110000]}
df = pd.DataFrame(data)

print(df.dtypes)