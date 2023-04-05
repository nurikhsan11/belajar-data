import pandas as pd
dataset=pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
print('Shape dataset:', dataset.shape)
print('\nLima data teratas:\n',dataset.head(5))
print('\nInformasi dataset:',dataset.info())
print(dataset.describe())
print('\nStatistik deskriptif:\n', dataset.describe())