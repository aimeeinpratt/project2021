#importing csv & json module
import csv
import pandas as pd

# csv file name
inp_filename = "MetObjects.csv"
out_filename = "artistandyear.csv"

#initializing the titles and rows list
Artist_Nationality = "American"


#readdata from csv
with open(inp_filename, 'r') as in_Met:
    reader = csv.DictReader(in_Met)
    ## CSV is open and reading ready
    #CSV is ready to output

    with open(out_filename,'w') as out_MET1:
        writer= csv.writer(out_MET1)
        writer.writerow(['Label','Label2'])
        
        for row in reader:
            artistcol = row['Artist Display Name']
            year = row['Object Begin Date']
            Object = row['Title']

            if 'Modern and Contemporary Art' in row ['Department'] and Artist_Nationality in row['Artist Nationality']: 
            
                writer.writerow([artistcol, year])

#panda merge and vlook

df1 = pd.read_csv ("artistandyear.csv")
df2 = pd.read_csv ("metartist-node.csv")

Outer_join1 = pd.merge(df1,df2, on='Label',how='outer')

Outer_join1.to_csv("merge1.csv", index=False)

df3 = pd.read_csv("merge1.csv")
df4 = pd.read_csv("Uniqueyearnode.csv")

Outer_join2 = pd.merge(df3,df4, on='Label2', how='outer')

Outer_join2.to_csv("Edge2.csv",index=False)






            


#row['Department'], row['Title'],row['Artist Display Name'], row['Object Begin Date'],row['Medium'], row['Dimensions']
#                if row['Artist Display Name'] not in Artsit: 
#                    Artsit.append(row['Artist Display Name'])