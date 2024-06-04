import pandas as pd

df = pd.read_csv('')

df.head()
df.tail(3)

df.info()
df.describe()

df.columns
df.index

df.loc[0, 'col name']
df.iloc[0, 0]

df.drop('col name', axis=1) # col
df.drop(0, axis=0)

grouped_df = df.groupby('colname').mean()