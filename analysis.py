from pymongo import MongoClient
import unicodecsv
import io

# Connect to database
client = MongoClient('localhost', 27017)
db = client.nhlstats
collection = db.players

with io.open('overall.csv', 'w', encoding='utf8') as csvfile:
    spamwriter = unicodecsv.DictWriter(csvfile, [u"LAST", u"FIRST", u"GP", u"G", u"GPG", u"A", u"APG", u"PPP", u"PPPPG", u"SOG", u"SOGPG", u"FOW", u"FOWPG", u"BLK", u"BLKPG", u"HTS", u"HTSPG", u"PIM", u"PIMPG", u"Year"])
    for player in collection.find():
        player[u'Overall'].update({u'FIRST': player['firstName'], u'LAST': player['lastName']})
        spamwriter.writerow(player[u'Overall'])


