from xlrd import open_workbook, cellname
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
		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(self.dataLegend)
		
	def evaluateValue(self, rowNumber, valueMap):
		if 'columnNumber' in valueMap:
			return self.sheetObjects[valueMap['sheetNumber']].cell(rowNumber, valueMap['columnNumber']).value
		else:
			# evaluate expression
			if valueMap['expression']['operation'] == '+':
				return self.evaluateValue(rowNumber, valueMap['expression']['operandA']) + self.evaluateValue(rowNumber, valueMap['expression']['operandB'])
			else:
				return 'Unimplemented expression'			
		
 	def lookupValue(self, playerKey, valueKey):
		# lookup key column for sheet where value resides
		valueMap = self.dataMap[valueKey]
		sheetMap = self.sheetsWithData[valueMap['sheetNumber']]
		for rowNumber in range(self.sheetObjects[valueMap['sheetNumber']].nrows):
			if playerKey == self.sheetObjects[valueMap['sheetNumber']].cell(rowNumber, sheetMap['sheetKeyColumn']).value:
				return self.evaluateValue(rowNumber, valueMap)