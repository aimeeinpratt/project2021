import csv
import pandas as pd
import re

inp_filename = "artworks.csv"
out_filename = "artistyear-wh.csv"

#------------
Uniqueyear = []
Uniqueartist = []
Museum = "Whitney"
artist_id_lookup = {}
unique_artist_id_number = 2173

#------------

#read data from csv
with open(inp_filename, 'r', newline='') as in_WH:

    reader = csv.DictReader(in_WH)

    with open(out_filename, 'w', newline='') as out_WH:
        writer = csv.writer(out_WH)
        writer.writerow(['Artist','Year'])

        for row in reader:

            artistcol = row['artists']
            initial_date = row['display_date']
            new_date1 = re.sub(r"[c]+.", '', initial_date)
            new_date2 = re.sub(r"[–]+[0-9]+[0-9]+[0-9]+[0-9]",'',new_date1)
            new_date3 = re.sub(r"[,].+[aA-zZ].+[0-9]",'',new_date2)
            new_date4 = re.sub(r"[,].+[a-z]",'',new_date3)
            new_date5 = re.sub(r"November, ",'',new_date4)
            new_date6 = re.sub(r"[bB]efore",'',new_date5)
            new_date7 = re.sub(r"After",'',new_date6)
            new_date8 = re.sub(r" refabrited +[0-9][0-9]",'',new_date7)
            new_date9 = re.sub(r" mounted and resigned +[0-9][0-9]","",new_date8)
            new_date10 = re.sub(r" printed +[0-9][0-9][0-9][0-9]","",new_date9)
            new_date11 = re.sub(r" published 1972","",new_date10)
            new_date12 = re.sub(r"– [0-9][0-9][0-9][0-9]","",new_date11)
            new_date13 = re.sub(r" or+.+[0-9][0-9][0-9][0-9]","",new_date12)
            new_date14 = re.sub(r"–ongoing","",new_date13)
            new_date15 = re.sub(r"July 16, ","",new_date14)
            new_date16 = re.sub(r"[–]+[0-9]+[0-9]",'',new_date15)
            new_date17 = re.sub(r",  1969",'',new_date16)
            new_date18 = re.sub(r"–72",'',new_date17)
            new_date19 = re.sub(r"late ",'',new_date18)
            new_date20 = re.sub(r",",'',new_date19)	
            new_date21 = re.sub(r"–","",new_date20)
            final_date = re.sub(r"[/]+.+[0-9][0-9]",'',new_date21)
            final_date2 = final_date.strip ()


#            if final_date not in Uniqueyear:
#                Uniqueyear.append(final_date)
                   

            writer.writerow([artistcol,final_date2])

            #writer.writerow([clean_up_artist,artist_id_lookup[clean_up_artist]])

#-----------------------------------------------------
    
