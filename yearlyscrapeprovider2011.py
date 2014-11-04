import yearlyscrapeprovider

class YearlyScrapeProvider2011(yearlyscrapeprovider.YearlyScrapeProvider):
    baseUrl = 'http://www.nhl.com/ice/playerstats.htm?fetchKey=20122ALLSASALL&sort=player.bioFirstNameLastName'
    stats = {}

