import csv
import pandas as pd
import glob
import os

metartist = pd.read_csv("artistyear-wh.csv")
whitneyartist = pd.read_csv("artistyear-met.csv")

merged = pd.concat([metartist,whitneyartist])

merged.to_csv("bothartist.csv", index=False)


#------------------------------------------
inp_filename1 = "bothartist.csv"
out_filename1 = "bothartistid.csv"
uniqueartist_both = []
uniqueartist_both_id = 163
targetartistid = []
artistvlookup = {}


with open(inp_filename1, 'r', newline='') as in_Both:
    reader = csv.DictReader(in_Both)
   
    for row in reader:

        artistlist = row["Artist"]

        if row["Artist"] not in uniqueartist_both:
            uniqueartist_both.append(row["Artist"])

            artistvlookup[artistlist] = uniqueartist_both_id
            uniqueartist_both_id = uniqueartist_both_id + 1


with open(out_filename1, 'w', newline='') as out_Both:
    writer = csv.writer(out_Both)
    writer.writerow(['Artist','source'])

    for allartist in uniqueartist_both:
        writer.writerow([allartist, artistvlookup[allartist]])

#------------------------------------------

df1 = pd.read_csv("bothartist.csv")
df2 = pd.read_csv("bothartistid.csv")

Outer_join1 = pd.merge(df1,df2, on='Artist',how='outer')

Outer_join1.to_csv("mergeartist1.csv", index=False)


#------------------------------------------
