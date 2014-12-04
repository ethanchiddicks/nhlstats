from bs4 import BeautifulSoup
import urllib2
import re

class CurrentPlayerListProvider:
    playerList = {}

    def __init__(self):
        for page in range(1,20):
            url = "http://www.nhl.com/ice/playersearch.htm?season=20142015&pg=%s" % (page)
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
                self.playerList[id.group(0)] = {
                    'firstName': name.group(2),
                    'lastName': name.group(1)
                    }

    def getList(self):
        return self.playerList
