#Import library yang dibutuhkan
import pandas as pd

#Baca file dqlabregex.tsv
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')

#Ubah kata Sendja, dsb menjadi Senja pada kolom staf_pencatat
dqlabregex['staf_pencatat'] = dqlabregex['staf_pencatat'].str.replace('Sen.?ja', 'Senja')

#Tampilkan hasilnya
print(dqlabregex[['staf_pencatat']])