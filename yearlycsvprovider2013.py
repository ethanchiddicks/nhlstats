import os
import yearlycsvprovider


class YearlyCSVProvider2013(yearlycsvprovider.YearlyCSVProvider):
    sourceCSV = os.path.normpath("data/NHL 2013-14.xls")
    sheetObjects = {}
    sheetsWithData = {
        0: {'sheetKeyColumn': 13},
        1: {'sheetKeyColumn': 2},
        2: {'sheetKeyColumn': 2},
        3: {'sheetKeyColumn': 4},
    }
    dataLegend = {}
    dataMap = {
        'G': {'sheetNumber': 0, 'columnNumber': 21},
        'A': {'sheetNumber': 0, 'columnNumber': 22},
        'PPP': {'sheetNumber': 2, 'columnNumber': 8},
        'FOW': {'sheetNumber': 0, 'columnNumber': 44},
        'PIM': {'sheetNumber': 0, 'columnNumber': 60},
        'BLK': {'sheetNumber': 0, 'columnNumber': 50},
        'SOG': {'sheetNumber': 0, 'columnNumber': 25},
        'HTS': {'sheetNumber': 0, 'columnNumber': 49},
        'GP': {'sheetNumber': 0, 'columnNumber': 20},
        'FN': {'sheetNumber': 0, 'columnNumber': 14},
        'LN': {'sheetNumber': 0, 'columnNumber': 15},
        'AGE': {'sheetNumber': 0, 'columnNumber': 12},
    }