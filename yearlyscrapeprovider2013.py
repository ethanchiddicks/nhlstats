import yearlyscrapeprovider

class YearlyScrapeProvider2013(yearlyscrapeprovider.YearlyScrapeProvider):
    baseUrl = 'http://www.nhl.com/ice/playerstats.htm?fetchKey=20142ALLSASALL&sort=player.bioFirstNameLastName'
    stats = {}

