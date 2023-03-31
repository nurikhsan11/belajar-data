import pandas as pd

df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/sample_csv.csv')

print("Tiga data teratas:\n", [df.head(3)])
print("Tiga data terbawah:\n", [df.tail(3)])