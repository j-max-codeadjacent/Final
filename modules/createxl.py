
from openpyxl import Workbook
from openpyxl.compat import range

def create_workbook():
	wb = Workbook()
	ws1 = wb.active
	ws1.title = 'initialdata'
	ws1.sheet_properties.tabColor = "ffa500"
for row in range(1,40):
	ws1.append(['a','b'])
wb.save('novel_data.xlsx')