import pandas as pd

df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t")

print("Index:",df.index)

print("columns:", df.columns)