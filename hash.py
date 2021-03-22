import hashlib

def get_hashing(filename):
	with open(filename,"rb") as file:
		bytes = file.read() 
		hash = hashlib.sha256(bytes).hexdigest();
		print(hash)
		
	file.close()


Excel_file = '../data/System_Money.xlsx'
hash_file = '../data/hash.txt'

get_hashing(Excel_file)
"""
file = open(hash_file)
if(file.read() == None)


	print("file is empty")
"""
