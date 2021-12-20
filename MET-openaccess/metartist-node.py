#importing csv & json module
import csv
import json
from os import X_OK

# csv file name
inp_filename1 = "MetObjects.csv"
out_filename1 = "metartist-node.csv"
out_filename2 = "metartist-edge.csv"
out_filename3 = "metartist-id.csv"

#initializing the titles and rows list
Artist_Nationality = "American"

Duplicate_Artist = []
Unique_Artist = []
#----------------------- v lookup and create unique id
artist_id_lookup = {}
unique_artist_id_number = 3
#----------------------- output list
museumname1 = "MET"
museumid = "1"
typemet = "Directed"
Weightmet = "1"


#readdata from csv
## CSV is open and reading ready
with open(inp_filename1, 'r', newline='') as in_Met:

    reader = csv.DictReader(in_Met)

    for row in reader:

        if 'Modern and Contemporary Art' in row ['Department'] and Artist_Nationality in row['Artist Nationality']: 

            # for index in range (0,totaluni_count):

                if row['Artist Display Name'] not in Unique_Artist: 
                    Unique_Artist.append(row['Artist Display Name'])

                    artist_id_lookup[row['Artist Display Name']] = unique_artist_id_number
                    unique_artist_id_number = unique_artist_id_number + 1


                else:
                    Duplicate_Artist.append(row['Artist Display Name'])

                    totaluni_count = len(Unique_Artist)

                
                    # for v in Unique_Artist:
                    
                    #     writer.writerow([index,v])




#create node file
with open(out_filename1,'w') as out_MET1:

    writer= csv.writer(out_MET1)
    writer.writerow(['Label','id','node'])

    for artist in Unique_Artist:
        #print(artist)
        writer.writerow([artist,artist_id_lookup[artist],artist_id_lookup[artist]])














#row['Department'], row['Title'],row['Artist Display Name'], row['Object Begin Date'],row['Medium'], row['Dimensions']