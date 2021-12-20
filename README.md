# Project2021
Final Project-program cultural heritage
Looking at the contemporary art collections in the Met and Whitney Museum of Art, our project uses data visualization to analyze the relationships between their collections’ key variables: year, artwork, donor, and artist. Both datasets had more than 15 fields and over 20,000 rows that lessened to 15,000 after data cleaning. The datasets can be found here:
The Met: https://github.com/metmuseum/openaccess 
54 fields—focused on display_date, artists, and artworks
20,000 rows

Whitney Museum of Art: https://github.com/whitneymuseum/open-access
13 fields—focused on display_date, artists, and artworks
15,000 rows


The analysis was broken into two parts, using similar data cleaning processes in Python, yet different data visualization tools to narrate these relationships’ trends. Python was used for data cleaning, in which we went through a few rounds of data cleaning to isolate the right data needed to maneuver and identify the variables. Our data cleaning required:
Isolating the initial display year for each artwork
Filtering through the credit line for the donor names
Using Vlookup to configure nodes and edges within the edited dataset from Python

I created Networks graphs in Gephi to visualize similarities and differences between the variables within these collection.
Under the network, the variables I chose: Museums, Artist, Initial Display Name, and Credit Line.

My Process:
1. Filter by “Modern and Contemporary Art ” with “American Artist” (Only for MET dataset)
2. Create the different sheets:
    Museum vs Artists
    Museum vs Display Years
    Artist vs Display Years
    Artist vs Donor (MET)
    Unique Artist, Unique Display Year, Donor(MET) with Unique ID (node)
    Source and Target sheet between “Artist and Museum”, and “Artist and Display year”(Edge)
