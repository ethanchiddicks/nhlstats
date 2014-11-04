import yearlycsvprovider2011
import yearlycsvprovider2012
import yearlycsvprovider2013
import yearlyscrapeprovider2011
import yearlyscrapeprovider2012
import yearlyscrapeprovider2013
import yearlyscrapeprovider2014

class DataService:
    dataProviders = {
        '2011': yearlyscrapeprovider2011.YearlyScrapeProvider2011(),
        '2012': yearlyscrapeprovider2012.YearlyScrapeProvider2012(),
        '2013': yearlyscrapeprovider2013.YearlyScrapeProvider2013(),
        '2014': yearlyscrapeprovider2014.YearlyScrapeProvider2014()
    }
    dataAvailable = {}

    def __init__(self):
        self.dataAvailable['2011'] = self.dataProviders['2011'].getMap().keys()
        self.dataAvailable['2012'] = self.dataProviders['2012'].getMap().keys()
        self.dataAvailable['2013'] = self.dataProviders['2013'].getMap().keys()
        self.dataAvailable['2014'] = self.dataProviders['2014'].getMap().keys()

    def getDataAvailable(self):
        return self.dataAvailable

    def getYearlyData(self, playerReference, year):
        if year in self.dataAvailable:
            return self.dataProviders[year].getPlayerProfile(playerReference)
        else:
            raise NotImplementedError("No datasource for specified year")
