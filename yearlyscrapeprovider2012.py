import yearlyscrapeprovider

class YearlyScrapeProvider2012(yearlyscrapeprovider.YearlyScrapeProvider):
    baseUrl = 'http://www.nhl.com/ice/playerstats.htm?fetchKey=20132ALLSASALL&sort=player.bioFirstNameLastName'
    stats = {}

