import pandas as pd

df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/sample_tsv.tsv", sep="\t")

df_x = df.set_index(['order_date', "city", 'customer_id'])

for name, level in zip(df_x.index.names, df_x.index.levels):
    print(name,':',level)