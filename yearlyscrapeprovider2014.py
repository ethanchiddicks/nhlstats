import yearlyscrapeprovider

class YearlyScrapeProvider2014(yearlyscrapeprovider.YearlyScrapeProvider):
    baseUrl = 'http://www.nhl.com/ice/playerstats.htm?fetchKey=20152ALLSASALL&sort=player.bioFirstNameLastName'
    stats = {}

