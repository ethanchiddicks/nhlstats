from dataservice import DataService
from player import Player
from currentplayerlistprovider import CurrentPlayerListProvider
from pymongo import MongoClient

print 'Getting player list'
playerList = CurrentPlayerListProvider().getList()

# Connect to database
client = MongoClient('localhost', 27017)
db = client.nhlstats
collection = db.players

print 'Emptying database'
collection.remove()

ds = DataService()

for playerId, playerMeta in playerList.iteritems():
    print "Processing player %s" % playerId
    playerObject = Player(playerId, ds)
    playerData = playerObject.getStats()
    if playerData:
        playerData['_id'] = playerId
        playerData['firstName'] = playerMeta['firstName']
        playerData['lastName'] = playerMeta['lastName']

        collection.insert(playerData)