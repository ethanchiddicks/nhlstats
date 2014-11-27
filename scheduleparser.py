from pymongo import MongoClient
import os
import csv
from datetime import datetime

# Connect to database
client = MongoClient('localhost', 27017)
db = client.nhlstats
collection = db.nhlschedule


print 'Emptying database'
collection.remove()

sourceCSV = os.path.normpath("data/NHL Schedule 2014-15.csv")
with open(sourceCSV, 'rb') as csvfile:
    schedulereader = csv.reader(csvfile)
    next(schedulereader)
    for row in schedulereader:
        teams = row[0].split("@")
        gamedate = datetime.strptime(row[1], '%m/%d/%Y')
        game = {}
        game['homeTeam'] = teams[1].strip()
        game['visitingTeam'] = teams[0].strip()
        game['date'] = gamedate
        collection.insert(game)