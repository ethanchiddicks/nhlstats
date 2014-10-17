import os
import yearlycsvprovider


class YearlyCSVProvider2012(yearlycsvprovider.YearlyCSVProvider):
    sourceCSV = os.path.normpath("data/NHL 2012-13.xls")
    sheetObjects = {}
    sheetsWithData = {
        0: {'sheetKeyColumn': 10},
    }
    dataLegend = {}
    dataMap = {
        'G': {'sheetNumber': 0, 'columnNumber': 17},  # 15
        'A': {'sheetNumber': 0, 'columnNumber': 18},  #41
        'PPP': {'sheetNumber': 0, 'columnNumber': 144},  #17
        'FOW': {'sheetNumber': 0, 'columnNumber': 34},  #453
        'PIM': {'sheetNumber': 0, 'columnNumber': 48},  #16
        'BLK': {'sheetNumber': 0, 'columnNumber': 39},  #18
        'SOG': {'sheetNumber': 0, 'columnNumber': 21},  #124
        'HTS': {'sheetNumber': 0, 'columnNumber': 38},  #21
        'GP': {'sheetNumber': 0, 'columnNumber': 16},
        'AGE': {'sheetNumber': 0, 'columnNumber': 9},
    }