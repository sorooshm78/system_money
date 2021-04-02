import re

class Month:
	date = {
	1 : 'فروردین',
	2 : 'اردیبهشت',
	3 : 'خرداد',
	4 : 'تیر',
	5 : 'مرداد',
	6 : 'شهریور',
	7 : 'مهر',
	8 : 'ابان',
	9 : 'اذر',
	10: 'دی',
	11: 'بهمن',
	12: 'اسفند'
	} 

	def __init__(self, month):
		self.month = month
		self.name = Month.date[month]
		self.list_record = []
		self.allocation = 0
		self.expend = 0

	def add_record(self, comment, val, date):
		self.list_record.append({"comment" : comment, "val" : val, "date" : date})	
		self.expend += val
	
	def add_allocation(self, val):
		self.allocation += val

	def get_remaining(self):
		return self.allocation - self.expend



# Class Block
class Block:
	def __init__(self, name):
		self.name = name
		self.allocation = 0
		self.expend = 0 
		self.list_month = []
		for i in range(1, 13):
			self.list_month.append(Month(i))

	def add_allocation(self, val, date):		
		month = re.findall(r'.+/(.+)/.+', date)			
		self.list_month[int(month[0]) - 1].add_allocation(val)
		 
	def add_record(self, comment, val, date):
		month = re.findall(r'.+/(.+)/.+', date)			
		self.list_month[int(month[0]) - 1].add_record(comment, val, date)

	def get_total_expend(self):
		total_expend = 0
		for month in self.list_month:
			total_expend += month.expend
		return total_expend

	def get_total_alocation(self):
		total_alocation = 0
		for month in self.list_month:
			total_alocation += month.allocation
		return total_alocation

	def get_total_remaining(self):
		return self.get_total_alocation() - self.get_total_expend()
