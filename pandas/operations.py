import pandas as pd
import numpy as np
data=pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
data['C'] = data['A'] + data['B']
# print(data)
# print(data.shape)
# print(data.columns)
# print(data.dtypes)
# print(data.info())
print(data.describe())