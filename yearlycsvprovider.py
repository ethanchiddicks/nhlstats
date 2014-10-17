from xlrd import open_workbook
import pprint


class YearlyCSVProvider:
    def __init__(self):
        # open spreadsheet file
        self.book = open_workbook(self.sourceCSV)

        # get list of sheet and header information
        # iterate through all sheets and look for column values
        for sheetNumber in self.sheetsWithData:
            # load sheet
            self.sheetObjects[sheetNumber] = self.book.sheet_by_index(sheetNumber)

            self.dataLegend[sheetNumber] = {}

            # get fieldnames from first row
            for columnIndex in range(self.sheetObjects[sheetNumber].ncols):
                self.dataLegend[sheetNumber][columnIndex] = self.sheetObjects[sheetNumber].cell(0, columnIndex).value

    def printLegend(self):
        """Prints the list of column headings for building valueMaps."""
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.dataLegend)


    def lookupValue(self, playerKey, valueKey):
        """Lookup a value based on a player key and a statistic key."""
        valueMap = self.dataMap[valueKey]
        return self.lookupKey(playerKey, valueMap)

    def lookupKey(self, playerKey, valueMap):
        """Lookup a value based on a player key and a valueMap."""
        sheetMap = self.sheetsWithData[valueMap['sheetNumber']]
        for rowNumber in range(self.sheetObjects[valueMap['sheetNumber']].nrows):
            if playerKey == self.sheetObjects[valueMap['sheetNumber']].cell(rowNumber, sheetMap['sheetKeyColumn']).value:
                if 'columnNumber' in valueMap:
                    return self.sheetObjects[valueMap['sheetNumber']].cell(rowNumber, valueMap['columnNumber']).value
                else:
                    # evaluate expression, calling self to resolve composite expressions
                    if valueMap['expression']['operation'] == '+':
                        return self.lookupKey(playerKey, valueMap['expression']['operandA']) + self.lookupKey(playerKey, valueMap['expression']['operandB'])
                    elif valueMap['expression']['operation'] == '-':
                        return self.lookupKey(playerKey, valueMap['expression']['operandA']) - self.lookupKey(playerKey, valueMap['expression']['operandB'])
                    elif valueMap['expression']['operation'] == '/':
                        return self.lookupKey(playerKey, valueMap['expression']['operandA']) / self.lookupKey(playerKey, valueMap['expression']['operandB'])
                    elif valueMap['expression']['operation'] == '*':
                        return self.lookupKey(playerKey, valueMap['expression']['operandA']) * self.lookupKey(playerKey, valueMap['expression']['operandB'])
                    else:
                        raise NotImplementedError("Expression not implemented")

    def getPlayerProfile(self, playerKey):
        """Returns all mapped data about a player."""
        playerProfile = {}
        statKeys = []
        for statKey in self.dataMap:
            playerProfile[statKey] = self.lookupValue(playerKey, statKey)
            #if isinstance(playerProfile[statKey], (int, float)):
            if playerProfile[statKey].isnumeric():
                statKeys.append(statKey)
        # calculate rate stats
        for statKey in statKeys:
            playerProfile[statKey + 'PG'] = round(playerProfile[statKey] / playerProfile['GP'], 2)
        return playerProfile