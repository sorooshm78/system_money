# Class Block
class Block:
	def __init__(self, name):
		self.name = name
		self.allocation = 0
		self.expend = 0 
		self.list_record = []

	def print(self):
		print("Name:" + self.name +
		"\t allo:" +  str(self.allocation) +
		"\t expend:" + str(self.expend) +
		"\t remaining:" + str(self.get_remaining()))

		print("list records:")
		for record in self.list_record:	
			print("comment:" + record['comment'] +
			"\t val:" +  str(record['val']) +
			"\t date:" + record['date'])

	def add_expend(self, val):
		self.expend += val 

	def add_allocation(self, val):
		self.allocation += val 

	def get_remaining(self):
		return self.allocation - self.expend
	
	def add_record(self, comment, val, date):
		self.list_record.append({"comment" : comment,
								 "val" : val,
								 "date" : date})

	def sort_record(self, type = "val", reverse = False):
		def key_by_val(dict):
			return dict['val']

		def key_by_date(dict):
			return dict['date']

		if(type == "val"):
			if(reverse):
				self.list_record.sort(key=key_by_val, reverse = True)
			else:
				self.list_record.sort(key=key_by_val)
	
		if(type == "date"):
			if(reverse):
				self.list_record.sort(key=key_by_date, reverse = True)
			else:
				self.list_record.sort(key=key_by_date)
