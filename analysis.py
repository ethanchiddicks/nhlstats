from percentilerank import PercentileRank
from pymongo import MongoClient
from tabulate import tabulate


# Connect to database
client = MongoClient('localhost', 27017)
db = client.nhlstats
collection = db.players

GPG, APG, PPPPG, SOGPG, FOWPG, BLKPG, HTSPG, PIMPG = ([] for i in range(8))

for player in collection.find({"2014.GP": {"$gte": 1}}, {"2014.GPG": True, "lastName": True}).sort([("2014.GPG", 1)]):
    GPG.append(player['2014']['GPG'])
for player in collection.find({"2014.GP": {"$gte": 1}}, {"2014.APG": True, "lastName": True}).sort([("2014.APG", 1)]):
    APG.append(player['2014']['APG'])
for player in collection.find({"2014.GP": {"$gte": 1}}, {"2014.PPPPG": True, "lastName": True}).sort([("2014.PPPPG", 1)]):
    PPPPG.append(player['2014']['PPPPG'])
for player in collection.find({"2014.GP": {"$gte": 1}}, {"2014.SOGPG": True, "lastName": True}).sort([("2014.SOGPG", 1)]):
    SOGPG.append(player['2014']['SOGPG'])
for player in collection.find({"2014.GP": {"$gte": 1}, "2014.FOWPG": {"$gt": 1}}, {"2014.FOWPG": True, "lastName": True}).sort([("2014.FOWPG", 1)]):
    FOWPG.append(player['2014']['FOWPG'])
for player in collection.find({"2014.GP": {"$gte": 1}}, {"2014.BLKPG": True, "lastName": True}).sort([("2014.BLKPG", 1)]):
    BLKPG.append(player['2014']['BLKPG'])
for player in collection.find({"2014.GP": {"$gte": 1}}, {"2014.HTSPG": True, "lastName": True}).sort([("2014.HTSPG", 1)]):
    HTSPG.append(player['2014']['HTSPG'])
for player in collection.find({"2014.GP": {"$gte": 1}}, {"2014.PIMPG": True, "lastName": True}).sort([("2014.PIMPG", 1)]):
    PIMPG.append(player['2014']['PIMPG'])


GRank = PercentileRank(GPG)
ARank = PercentileRank(APG)
PPPRank = PercentileRank(PPPPG)
SOGRank = PercentileRank(SOGPG)
FOWRank = PercentileRank(FOWPG)
BLKRank = PercentileRank(BLKPG)
HTSRank = PercentileRank(HTSPG)
PIMRank = PercentileRank(PIMPG)

for player in collection.find({"2014.GP": {"$gt": 1}}):
    player["2014"]["GPGRank"] = GRank.getScore(player["2014"]["GPG"])
    player["2014"]["APGRank"] = ARank.getScore(player["2014"]["APG"])
    player["2014"]["PPPPGRank"] = PPPRank.getScore(player["2014"]["PPPPG"])
    player["2014"]["SOGPGRank"] = SOGRank.getScore(player["2014"]["SOGPG"])
    player["2014"]["FOWPGRank"] = FOWRank.getScore(player["2014"]["FOWPG"])
    player["2014"]["BLKPGRank"] = BLKRank.getScore(player["2014"]["BLKPG"])
    player["2014"]["HTSPGRank"] = HTSRank.getScore(player["2014"]["HTSPG"])
    player["2014"]["PIMPGRank"] = PIMRank.getScore(player["2014"]["PIMPG"])
    player["2014"]["2014Rank"] = player["2014"]["GPGRank"] +\
                                       player["2014"]["APGRank"] +\
                                       player["2014"]["PPPPGRank"] +\
                                       player["2014"]["SOGPGRank"] +\
                                       player["2014"]["FOWPGRank"] +\
                                       player["2014"]["BLKPGRank"] +\
                                       player["2014"]["HTSPGRank"] +\
                                       player["2014"]["PIMPGRank"]
    collection.update({"_id": player["_id"]}, player)


# Overall stats
GPG, APG, PPPPG, SOGPG, FOWPG, BLKPG, HTSPG, PIMPG = ([] for i in range(8))

for player in collection.find({"Overall.GP": {"$gte": 1}}, {"Overall.GPG": True, "lastName": True}).sort([("Overall.GPG", 1)]):
    GPG.append(player['Overall']['GPG'])
for player in collection.find({"Overall.GP": {"$gte": 1}}, {"Overall.APG": True, "lastName": True}).sort([("Overall.APG", 1)]):
    APG.append(player['Overall']['APG'])
for player in collection.find({"Overall.GP": {"$gte": 1}}, {"Overall.PPPPG": True, "lastName": True}).sort([("Overall.PPPPG", 1)]):
    PPPPG.append(player['Overall']['PPPPG'])
for player in collection.find({"Overall.GP": {"$gte": 1}}, {"Overall.SOGPG": True, "lastName": True}).sort([("Overall.SOGPG", 1)]):
    SOGPG.append(player['Overall']['SOGPG'])
for player in collection.find({"Overall.GP": {"$gte": 1}, "Overall.FOWPG": {"$gt": 1}}, {"Overall.FOWPG": True, "lastName": True}).sort([("Overall.FOWPG", 1)]):
    FOWPG.append(player['Overall']['FOWPG'])
for player in collection.find({"Overall.GP": {"$gte": 1}}, {"Overall.BLKPG": True, "lastName": True}).sort([("Overall.BLKPG", 1)]):
    BLKPG.append(player['Overall']['BLKPG'])
for player in collection.find({"Overall.GP": {"$gte": 1}}, {"Overall.HTSPG": True, "lastName": True}).sort([("Overall.HTSPG", 1)]):
    HTSPG.append(player['Overall']['HTSPG'])
for player in collection.find({"Overall.GP": {"$gte": 1}}, {"Overall.PIMPG": True, "lastName": True}).sort([("Overall.PIMPG", 1)]):
    PIMPG.append(player['Overall']['PIMPG'])

GRank = PercentileRank(GPG)
ARank = PercentileRank(APG)
PPPRank = PercentileRank(PPPPG)
SOGRank = PercentileRank(SOGPG)
FOWRank = PercentileRank(FOWPG)
BLKRank = PercentileRank(BLKPG)
HTSRank = PercentileRank(HTSPG)
PIMRank = PercentileRank(PIMPG)

for player in collection.find({"Overall.GP": {"$gt": 1}}):
    player["Overall"]["GPGRank"] = GRank.getScore(player["Overall"]["GPG"])
    player["Overall"]["APGRank"] = ARank.getScore(player["Overall"]["APG"])
    player["Overall"]["PPPPGRank"] = PPPRank.getScore(player["Overall"]["PPPPG"])
    player["Overall"]["SOGPGRank"] = SOGRank.getScore(player["Overall"]["SOGPG"])
    player["Overall"]["FOWPGRank"] = FOWRank.getScore(player["Overall"]["FOWPG"])
    player["Overall"]["BLKPGRank"] = BLKRank.getScore(player["Overall"]["BLKPG"])
    player["Overall"]["HTSPGRank"] = HTSRank.getScore(player["Overall"]["HTSPG"])
    player["Overall"]["PIMPGRank"] = PIMRank.getScore(player["Overall"]["PIMPG"])
    player["Overall"]["OverallRank"] = player["Overall"]["GPGRank"] +\
                                       player["Overall"]["APGRank"] +\
                                       player["Overall"]["PPPPGRank"] +\
                                       player["Overall"]["SOGPGRank"] +\
                                       player["Overall"]["FOWPGRank"] +\
                                       player["Overall"]["BLKPGRank"] +\
                                       player["Overall"]["HTSPGRank"] +\
                                       player["Overall"]["PIMPGRank"]
    collection.update({"_id": player["_id"]}, player)
    
    

header = ['ID',
          'LastName',
          'FirstName',
          'GP (14)',
          'GP (Ovrl)',
          'OverallRank (14)',
          'OverallRank (Ovrl)',
          'GPGRank (14)',
          'GPGRank (Ovrl)',
          'APGRank (14)',
          'APGRank (Ovrl)',
          'PPPPGRank (14)',
          'PPPPGRank (Ovrl)',
          'SOGPGRank (14)',
          'SOGPGRank (Ovrl)',
          'FOWPGRank (14)',
          'FOWPGRank (Ovrl)',
          'BLKPGRank (14)',
          'BLKPGRank (Ovrl)',
          'HTSPGRank (14)',
          'HTSPGRank (Ovrl)',
          'PIMPGRank (14)',
          'PIMPGRank (Ovrl)']
table = []

for player in collection.find({"2014.GP": {"$gt": 1}, "Overall.GP": {"$gt": 50}}, {"Overall": True, "2014": True, "lastName": True, "firstName": True}).sort([("Overall.OverallRank", -1)]):
    row = []
    row.append(player["_id"])
    row.append(player["lastName"])
    row.append(player["firstName"])
    row.append(str(player["2014"]["GP"]))
    row.append(str(player["Overall"]["GP"]))
    row.append(str(player["2014"]["2014Rank"]))
    row.append(str(player["Overall"]["OverallRank"]))
    row.append(str(player["2014"]["GPGRank"]))
    row.append(str(player["Overall"]["GPGRank"]))
    row.append(str(player["2014"]["APGRank"]))
    row.append(str(player["Overall"]["APGRank"]))
    row.append(str(player["2014"]["PPPPGRank"]))
    row.append(str(player["Overall"]["PPPPGRank"]))
    row.append(str(player["2014"]["SOGPGRank"]))
    row.append(str(player["Overall"]["SOGPGRank"]))
    row.append(str(player["2014"]["FOWPGRank"]))
    row.append(str(player["Overall"]["FOWPGRank"]))
    row.append(str(player["2014"]["BLKPGRank"]))
    row.append(str(player["Overall"]["BLKPGRank"]))
    row.append(str(player["2014"]["HTSPGRank"]))
    row.append(str(player["Overall"]["HTSPGRank"]))
    row.append(str(player["2014"]["PIMPGRank"]))
    row.append(str(player["Overall"]["PIMPGRank"]))
    table.append(row)
print ','.join(header)
for row in table:
    print ','.join(row)

