import pyreadr
import pandas as pd

result = pyreadr.read_r('data/data_censored.rda')
data = result['data_censored']
df = pd.DataFrame(data)
df.to_csv('data/data_censored.csv', index=False)