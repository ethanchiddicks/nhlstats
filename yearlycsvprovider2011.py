import os
import yearlycsvprovider


class YearlyCSVProvider2011(yearlycsvprovider.YearlyCSVProvider):
    sourceCSV = os.path.normpath("data/NHL 2011-12.xls")
    sheetObjects = {}
    sheetsWithData = {
        0: {'sheetKeyColumn': 1},
    }
    dataLegend = {}
    dataMap = {
        'G': {'sheetNumber': 0, 'columnNumber': 19},  # 8
        'A': {'sheetNumber': 0, 'columnNumber': 20},  #29
        'PPP': {'sheetNumber': 0, 'expression': {'operandA': {'sheetNumber': 0, 'columnNumber': 61}, 'operation': '+',
                                                 'operandB': {'sheetNumber': 0, 'columnNumber': 62}}},  #11
        'FOW': {'sheetNumber': 0, 'columnNumber': 38},  #227
        'PIM': {'sheetNumber': 0, 'columnNumber': 23},  #14
        'BLK': {'sheetNumber': 0, 'columnNumber': 28},  #7
        'SOG': {'sheetNumber': 0, 'columnNumber': 24},  #75
        'HTS': {'sheetNumber': 0, 'columnNumber': 27},  #11
        'GP': {'sheetNumber': 0, 'columnNumber': 18},  #22
        'AGE': {'sheetNumber': 0, 'columnNumber': 9},
    }