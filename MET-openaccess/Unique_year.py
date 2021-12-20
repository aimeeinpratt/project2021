#importing csv & json module
import csv
import json

# csv file name
inp_filename = "MetObjects.csv"
out_filename1 = "Uniqueyearnode.csv"
out_filename2 = "Uniqueyearedge.csv"
out_filename3 = "uniqueyear-met.csv"


#initializing the titles and rows list
Artist_Nationality = "American"
Unique_year = []

#----------------------- v lookup and create unique id
year_id_lookup = {}
unique_year_id_number = 2013

#----------------------- output list
museumname1 = "MET"
museumid = "1"
typemet = "Directed"
Weightmet = "1"

#readdata from csv
with open(inp_filename, 'r') as in_Met:

    reader = csv.DictReader(in_Met)
   
       ## CSV is open and reading ready
    for row in reader:

        artistcol = row['Artist Display Name']
        year = row['Object Begin Date']
        Object = row['Title']

        if 'Modern and Contemporary Art' in row ['Department'] and Artist_Nationality in row['Artist Nationality']: 
            if row['Object Begin Date'] not in Unique_year:
                Unique_year.append(row['Object Begin Date'])

                year_id_lookup[row['Object Begin Date']] = unique_year_id_number
                unique_year_id_number = unique_year_id_number + 1

# output yearnode
with open(out_filename1,'w') as out_MET1:
    writer= csv.writer(out_MET1)
    writer.writerow(['Label2', 'id', 'node'])
   
    for uniyear in Unique_year:
        writer.writerow([uniyear,year_id_lookup[uniyear],year_id_lookup[uniyear]])
            
# output year and met edge         
with open(out_filename2,'w') as out_MET2:
    writer= csv.writer(out_MET2)
    writer.writerow(['Label','Museum','source','target','Type','Weight'])

    for uniyear in Unique_year:
        writer.writerow([uniyear,museumname1,museumid,year_id_lookup[uniyear],typemet,Weightmet])


# output yearnode
with open(out_filename3,'w') as out_MET3:
    writer= csv.writer(out_MET3)
    writer.writerow(['Label2'])
   
    for uniyear in Unique_year:
        writer.writerow([uniyear,museumname1])


#row['Department'], row['Title'],row['Artist Display Name'], row['Object Begin Date'],row['Medium'], row['Dimensions']
#                if row['Artist Display Name'] not in Artsit: 
#                    Artsit.append(row['Artist Display Name'])