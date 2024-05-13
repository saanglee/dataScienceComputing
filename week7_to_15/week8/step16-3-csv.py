import numpy as np
import pandas as pd

df = pd.read_csv('kborank.csv')
print(df)
# print('columns: ', df.columns)
# print('index', df.index)
# print(df['2022'])

# 새로운 열 만들기

df['average'] = df.mean(axis=1)
df['average_3'] = (df['2020'] + df['2021'] + df['2022']) / 3
print(df)