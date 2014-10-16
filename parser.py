import yearlycsvprovider2011
import yearlycsvprovider2012
import yearlycsvprovider2013

provider2011 = yearlycsvprovider2011.YearlyCSVProvider2011()
provider2012 = yearlycsvprovider2012.YearlyCSVProvider2012()
provider2013 = yearlycsvprovider2013.YearlyCSVProvider2013()

#print provider2011.lookupValue('SIDNEYCROSBY', 'SOG')
provider2013.printLegend()