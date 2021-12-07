#importing csv & json module
import csv
import json
from os import X_OK

# csv file name
inp_filename = "MetObjects.csv"
out_filename = "metartist-node.csv"

#initializing the titles and rows list
Artist_Nationality = "American"
Duplicate_Artist = []
Unique_Artist = []

artist_id_lookup = {}
unique_artist_id_number = 0

#museumrow = 'MET'

#readdata from csv
## CSV is open and reading ready
with open(inp_filename, 'r', newline='') as in_Met:

    reader = csv.DictReader(in_Met)

    for row in reader:

        if 'Modern and Contemporary Art' in row ['Department'] and Artist_Nationality in row['Artist Nationality']: 

            if row['Artist Display Name'] not in Unique_Artist: 
                Unique_Artist.append(row['Artist Display Name'])

                artist_id_lookup[row['Artist Display Name']] = unique_artist_id_number
                unique_artist_id_number = unique_artist_id_number + 1

            else:
                Duplicate_Artist.append(row['Artist Display Name'])

                
                    # for v in Unique_Artist:
                    
                    # writer.writerow([index,v])

with open(out_filename,'w') as out_MET:

    writer= csv.writer(out_MET)
    writer.writerow(['id','Artist'])

    for artist in Unique_Artist:
        print(artist)
        writer.writerow([unique_artist_id_number[artist],artist])








#row['Department'], row['Title'],row['Artist Display Name'], row['Object Begin Date'],row['Medium'], row['Dimensions']