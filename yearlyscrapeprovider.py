from bs4 import BeautifulSoup
import urllib2
import re


class YearlyScrapeProvider:
    statsAvailable = {
        'G': {'viewName': 'summary', 'columnName': 'G'},
        'A': {'viewName': 'summary', 'columnName': 'A'},
        'PPP': {'viewName': 'summary', 'columnName': 'PPP'},
        'FOW': {'viewName': 'rtssPlayerStats', 'columnName': 'FOW'},
        'PIM': {'viewName': 'summary', 'columnName': 'PIM'},
        'BLK': {'viewName': 'rtssPlayerStats', 'columnName': 'BkS'},
        'SOG': {'viewName': 'summary', 'columnName': 'S'},
        'HTS': {'viewName': 'rtssPlayerStats', 'columnName': 'Hits'},
        'GP': {'viewName': 'summary', 'columnName': 'GP'},
    }

    def __init__(self):
        # Collapse view names
        views = {}
        for stat, meta in self.statsAvailable.iteritems():
            views[meta['viewname']]

        for page in range(1,25):
            url = self.baseURL + "&pg=%s" % (page)
            print url
            html = urllib2.urlopen(url).read()
            soup = BeautifulSoup(html)
            body = soup.find("tbody")
            if body is None:
                break
            rows = body.find_all("tr")

            for row in rows:
                cells = row.find_all("td")
                link = cells[0].find("a")
                idpattern = r'\d+'
                namepattern = r'([\w\s\-\'\.]+), ([\w\.]+)'
                idregex = re.compile(idpattern, re.UNICODE)
                nameregex = re.compile(namepattern, re.UNICODE)
                id = idregex.search(link.attrs[u'href'])
                name = nameregex.search(link.text.strip())
                print id.group(0), name.group(1), name.group(2)

    def getMap(self):
        """Returns a list of data sources available from this provider"""
        return self.statsAvailable

    def getPlayerProfile(self, playerKey):
        """Returns all mapped data about a player."""
        playerProfile = {}
        statKeys = []
        for statKey in self.dataMap:
            playerProfile[statKey] = self.lookupValue(playerKey, statKey)
            statKeys.append(statKey)
        return player