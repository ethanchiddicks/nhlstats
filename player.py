from tabulate import tabulate

class Player:
    #stats = {}
    #dataAvailable = {}
    #playerReference = ''
    statKey = {
        'Year': {'counting': False, 'rateable': False},
        'GP': {'counting': True, 'rateable': False},
        #'AGE': {'counting': False, 'rateable': False},
        'G': {'counting': True, 'rateable': True},
        'A': {'counting': True, 'rateable': True},
        'PPP': {'counting': True, 'rateable': True},
        'FOW': {'counting': True, 'rateable': True},
        'SOG': {'counting': True, 'rateable': True},
        'PIM': {'counting': True, 'rateable': True},
        'BLK': {'counting': True, 'rateable': True},
        'HTS': {'counting': True, 'rateable': True},
    }

    def __init__(self, playerReference, dataService):
        self.stats = {}
        self.playerReference = playerReference
        # Get all information the dataService can offer
        self.dataAvailable = dataService.getDataAvailable()
        for key in self.dataAvailable.iterkeys():
            self.stats[key] = dataService.getYearlyData(playerReference, key)
            self.stats[key]['Year'] = key
        self.tallyOverall()
        self.calculateRates()

    def tallyOverall(self):
        overallValues = {}
        for statKey, statMeta in self.statKey.iteritems():
            overall = 0.00
            if statMeta['counting']:
                for value in self.stats.itervalues():
                    try:
                        overall += float(value[statKey])
                    except TypeError:
                        overall += 0
            else:
                overall = 'N/A'
            overallValues[statKey] = overall
        self.stats['Overall'] = overallValues
        self.stats['Overall']['Year'] = 'Overall'

    def calculateRates(self):
        newStatKeys = {}
        for yearKey, yearValue in self.stats.iteritems():
            newStats = {}
            for statKey, statMeta in self.statKey.iteritems():
                if statMeta['rateable']:
                    rateKey = statKey + 'PG'
                    newStatKeys[rateKey] = {'calculated': True, 'counting': False, 'rateable': False}
                    try:
                        newStats[rateKey] = round(float(yearValue[statKey]) / float(yearValue['GP']), 2)
                    except TypeError:
                        newStats[rateKey] = None
            self.stats[yearKey].update(newStats)
        self.statKey.update(newStatKeys)


    def printYearOnYear(self):
        """Prints player's statistics, year-on-year"""
        # Get all values available.
        header = self.statKey.keys()
        header.sort()
        table = []
        for yearKey, yearValue in self.stats.iteritems():
            row = []
            for value in header:
                row.append(yearValue[value])
            table.append(row)
        print self.playerReference
        print tabulate(table, header, tablefmt="grid")

    def printOverall(self):
        """Prints player's overall statistics"""
        # Get all values available.
        header = self.statKey.keys()
        header.sort()
        table = []
        row = []
        for value in header:
            row.append(self.stats['Overall'][value])
        table.append(row)
        print self.playerReference
        print tabulate(table, header, tablefmt="grid")

    def getStats(self):
        return self.stats


