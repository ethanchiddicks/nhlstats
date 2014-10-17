import yearlycsvprovider2011
import yearlycsvprovider2012
import yearlycsvprovider2013
from tabulate import tabulate

provider2011 = yearlycsvprovider2011.YearlyCSVProvider2011()
provider2012 = yearlycsvprovider2012.YearlyCSVProvider2012()
provider2013 = yearlycsvprovider2013.YearlyCSVProvider2013()

playerProfile2011 = provider2011.getPlayerProfile('ERIKKARLSSON')
playerProfile2012 = provider2012.getPlayerProfile('ERIKKARLSSON')
playerProfile2013 = provider2013.getPlayerProfile('ERIKKARLSSON')


table = []
table.append([
    '2011',
    playerProfile2011['GP'],
    playerProfile2011['AGE'],
    playerProfile2011['G'],
    playerProfile2011['GPG'],
    playerProfile2011['A'],
    playerProfile2011['APG'],
    playerProfile2011['PPP'],
    playerProfile2011['PPPPG'],
    playerProfile2011['FOW'],
    playerProfile2011['FOWPG'],
    playerProfile2011['SOG'],
    playerProfile2011['SOGPG'],
    playerProfile2011['PIM'],
    playerProfile2011['PIMPG'],
    playerProfile2011['BLK'],
    playerProfile2011['BLKPG'],
    playerProfile2011['HTS'],
    playerProfile2011['HTSPG'],
])

table.append([
    '2012',
    playerProfile2012['GP'],
    playerProfile2012['AGE'],
    playerProfile2012['G'],
    playerProfile2012['GPG'],
    playerProfile2012['A'],
    playerProfile2012['APG'],
    playerProfile2012['PPP'],
    playerProfile2012['PPPPG'],
    playerProfile2012['FOW'],
    playerProfile2012['FOWPG'],
    playerProfile2012['SOG'],
    playerProfile2012['SOGPG'],
    playerProfile2012['PIM'],
    playerProfile2012['PIMPG'],
    playerProfile2012['BLK'],
    playerProfile2012['BLKPG'],
    playerProfile2012['HTS'],
    playerProfile2012['HTSPG'],
])

table.append([
    '2013',
    playerProfile2013['GP'],
    playerProfile2013['AGE'],
    playerProfile2013['G'],
    playerProfile2013['GPG'],
    playerProfile2013['A'],
    playerProfile2013['APG'],
    playerProfile2013['PPP'],
    playerProfile2013['PPPPG'],
    playerProfile2013['FOW'],
    playerProfile2013['FOWPG'],
    playerProfile2013['SOG'],
    playerProfile2013['SOGPG'],
    playerProfile2013['PIM'],
    playerProfile2013['PIMPG'],
    playerProfile2013['BLK'],
    playerProfile2013['BLKPG'],
    playerProfile2013['HTS'],
    playerProfile2013['HTSPG'],
])
    
    
    
headers = ['Year', 'GP', 'AGE', 'G', 'GPG', 'A', 'APG', 'PPP', 'PPPPG', 'FOW', 'FOWPG', 'SOG', 'SOGPG', 'PIM', 'PIMPG', 'BLK', 'BLKPG', 'HTS', 'HTSPG']
print tabulate(table, headers, tablefmt="grid")
#provider2013.printLegend()