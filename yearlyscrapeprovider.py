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
        self.stats = {}
        for stat, meta in self.statsAvailable.iteritems():
            if meta['viewName'] not in views:
                views[meta['viewName']] = []
                views[meta['viewName']].append([meta['columnName']])
            else:
                views[meta['viewName']].append([meta['columnName']])
        for viewName, columnArray in views.iteritems():
            for page in range(1,30):
                url = self.baseUrl + "&viewName=%s&pg=%s" % (viewName, page)
                print url
                html = urllib2.urlopen(url).read()
                soup = BeautifulSoup(html)
                header = soup.find("thead")
                if header is None:
                    break
                columns = header.find_all("th")
                statMap = []
                for column in columns:
                    statMap.append(column.text.strip())
                body = soup.find("tbody")
                rows = body.find_all("tr")
                for row in rows:
                    columnIndex = 0
                    cells = row.find_all("td")
                    rowKey = 0
                    for cell in cells:
                        if columnIndex is not 0:
                            if columnIndex is 1:
                                link = cell.find("a")
                                idpattern = r'\d+'
                                idregex = re.compile(idpattern, re.UNICODE)
                                id = idregex.search(link.attrs[u'href'])
                                rowKey = id.group(0)
                                if rowKey not in self.stats:
                                    self.stats[rowKey] = {}
                                    self.stats[rowKey]['Name'] = cell.text
                            else:
                                self.stats[rowKey][statMap[columnIndex]] = cell.text
                        columnIndex += 1

    def getMap(self):
        """Returns a list of data sources available from this provider"""
        return self.statsAvailable

    def getPlayerProfile(self, playerKey):
        """Returns all mapped data about a player."""
        player = {}
        if playerKey in self.stats:
            for stat, meta in self.statsAvailable.iteritems():
                player[stat] = int(self.stats[playerKey][meta['columnName']])
        return player