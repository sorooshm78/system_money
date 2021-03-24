import pandas
import openpyxl
from openpyxl import Workbook


class Input:
	def __init__(self, file, sheet):
		self.Data = pandas.read_excel(file, sheet_name = sheet)
	




Excel_file = '../data/System_Money.xlsx'
Sheet_name = 'blocks'

Block_Data = Input(Excel_file, Sheet_name)


"""
# Initialize variable from Excel
Excel_file = '../data/System_Money.xlsx'
Block_Data = pandas.read_excel(Excel_file, sheet_name = 'blocks')
Expend_Data = pandas.read_excel(Excel_file, sheet_name = 'expend')
Allocation_Data = pandas.read_excel(Excel_file, sheet_name = 'allocation')

# Initialize list obj blocks from Excel
List_Block = []

for index_row, row in Block_Data.iterrows():
    List_Block.append(Block(row['Name']))
"""
