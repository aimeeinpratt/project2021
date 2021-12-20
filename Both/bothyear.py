import csv
import pandas as pd
import glob
import os

metyear = pd.read_csv("uniqueyear-met.csv")
whitneyear = pd.read_csv("uniqueyear-wh.csv")

merged = pd.concat([metyear,whitneyear])

merged.to_csv("bothyear.csv", index=False)


#------------------------------------------
inp_filename1 = "bothyear.csv"
out_filename1 = "bothyearid.csv"
uniqueyear_both = []
uniqueyear_both_id = 1
targetyearid = []
yearvlookup = {}


with open(inp_filename1, 'r', newline='') as in_Both:
    reader = csv.DictReader(in_Both)

   
    for row in reader:

        yearlist = row["Label2"]

        if row["Label2"] not in uniqueyear_both:
            uniqueyear_both.append(row["Label2"])

            yearvlookup[yearlist] = uniqueyear_both_id
            uniqueyear_both_id = uniqueyear_both_id + 1


with open(out_filename1, 'w', newline='') as out_Both:
    writer = csv.writer(out_Both)
    writer.writerow(['Label2','source'])

    for allyear in uniqueyear_both:
        writer.writerow([allyear, yearvlookup[allyear] ])

#------------------------------------------

df1 = pd.read_csv("bothyear.csv")
df2 = pd.read_csv("bothyearid.csv")

Outer_join1 = pd.merge(df1,df2, on='Label2',how='outer')

Outer_join1.to_csv("mergeboth1.csv", index=False)

df3 = pd.read_csv("mergeboth1.csv")
df4 = pd.read_csv("Museum-node.csv")

Outer_join2 = pd.merge(df3,df4, on='Unnamed: 1',how='outer')

Outer_join2.to_csv("edgeyearboth.csv", index=False)

#------------------------------------------
