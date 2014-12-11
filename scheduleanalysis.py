from pymongo import MongoClient
import yaml
from datetime import date, timedelta
from dateutil.rrule import rrule, DAILY

# Connect to database
client = MongoClient('localhost', 27017)
db = client.nhlstats
collection = db.nhlschedule

roster_file = open("roster/ethan09122014.yml", 'r')
roster = yaml.load(roster_file)

league_file = open("league/donkadonkadonka.yml", 'r')
league = yaml.load(league_file)

start_date = date(2014, 12, 9)
end_date = date(2015, 12, 9)

slots_available = {}
for position in league['positions']:
    slots_available[position['position']] = position['slots']

for this_day in rrule(DAILY, dtstart=start_date, until=end_date):
    print this_day.isoformat()
    next_day = this_day + timedelta(days=1)
    teams_playing = []
    players_playing = []
    slots_available = {}
    for game in collection.find({"date": {"$gte": this_day, "$lt": next_day}}):
        teams_playing.append(game['visitingTeam'])
        teams_playing.append(game['homeTeam'])
    for player in roster['players']:
        if player['team'] in teams_playing:
            players_playing.append(player)



