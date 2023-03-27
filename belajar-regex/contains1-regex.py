import pandas as pd

dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv" ,sep = '\t')
dqlabregex['kota_awalan_j_s'] = dqlabregex['kota'].str.contains('^(j|s)' , case = False)

print(dqlabregex[['kota','kota_awalan_j_s']])