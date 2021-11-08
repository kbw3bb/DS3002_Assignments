import json
import csv
import requests
import pandas as pd

#1
# Fetch / download / retrieve a remote data file by URL, S3 key, or ingest a local file mounted.
#I decided to use a local csv file on my computer, thats being read in from a raw data on github
nfl = pd.read_csv("https://raw.githubusercontent.com/kbw3bb/DS3002_Assignments/main/nfl2008_fga.csv")
nfl.head()

#3
# Modify number of columns
# Take away the season column since the data is entirely from the 2008 season
nfl.drop('season', inplace=True, axis=1)
nfl.head()

#5. Generate a brief summary of the data file ingestion including: Number of records and Number of columns
row_summary =len(nfl.axes[0])
column_summary=len(nfl.axes[1])
print("Number of Rows: "+str(row_summary))
print("Number of Columns: "+str(column_summary))

#2 / #4
# Convert the general format and data structure of the data source (from CSV to JSON), write to disk
# 2 WAYS:
#1st way:
nfl1 = nfl.to_json(orient="split") #This converts the input to json, labeled Data1
nfl_parsed = json.loads(nfl1)  #This parses Data1
loaded_json = json.dumps(nfl_parsed, indent=4) #This loads the parsed data into a json file
with open('pipeline.json', 'w') as file_js:
    json.dump(loaded_json, file_js)
    #This writes the json to a local json file

#2nd way using A function, using local file paths on my computer for the data
#The arguments are file paths above
def make_json(csv_file_path, json_file_path):
    #Create an empty dictionary
    data_to_use = []
    #open csv reader called Dictreader, loads the csv file data
    with open(csv_file_path, encoding='utf-8') as csv_file:
        csvReader = csv.DictReader(csv_file)
        #Now convert each row into a dictionary and add to the data
        for rows in csvReader:
            data_to_use.append(rows)
    #Open a json writer and use json.dumps to dump data
    #ultimately converts file to json string and writes to file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data_to_use, indent = 4))
#specify the two file paths according to my computer
csv_file_path = r'/Users/kentwilliams/Desktop/DS-3001/data/nfl2008_fga.csv'
json_file_path = r'/Users/kentwilliams/Desktop/DS-3001/data/nfl2008_fga.csv'
make_json(csv_file_path, json_file_path) #Now call the function to use and convert/write

#Code shows no errors when run, so no informative messages needed