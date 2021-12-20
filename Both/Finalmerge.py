import csv
import pandas as pd


df3 = pd.read_csv("mergeartist1.csv")
df4 = pd.read_csv("bothyearid.csv")


Outer_join = pd.merge(df3,df4, on='label',how='outer')

Outer_join.to_csv("edgeartistboth.csv", index=False)