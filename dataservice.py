import yearlycsvprovider2011
import yearlycsvprovider2012
import yearlycsvprovider2013

class DataService:
    dataProviders = {
        '2011': yearlycsvprovider2011.YearlyCSVProvider2011(),
        '2012': yearlycsvprovider2012.YearlyCSVProvider2012(),
        '2013': yearlycsvprovider2013.YearlyCSVProvider2013(),
    }
    dataAvailable = {}

    def __init__(self):
        self.dataAvailable['2011'] = self.dataProviders['2011'].getMap().keys()
        self.dataAvailable['2012'] = self.dataProviders['2012'].getMap().keys()
        self.dataAvailable['2013'] = self.dataProviders['2013'].getMap().keys()

    def getDataAvailable(self):
        return self.dataAvailable

    def getYearlyData(self, playerReference, year):
        if year in self.dataAvailable:
            return self.dataProviders[year].getPlayerProfile(playerReference)
        else:
            raise NotImplementedError("No datasource for specified year")
