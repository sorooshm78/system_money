import hashlib
import os
import sys

# Function
def get_hash_file(file_name):
	with open(file_name,"rb") as file:
		bytes = file.read() 
		hash = hashlib.sha256(bytes).hexdigest();
		return hash

def write_hash_to_file(Hash_file):
	write_file = open(Hash_file, "w")
	write_file.write(get_hash_file(Excel_file))	
	write_file.close()	
	print("Write Excel hash to file")

def run_analyze_file():
	os.system("python3 Analyze.py")
	print("Run Analyze.py")

# Path file
Excel_file = "../data/System_Money.xlsx"
Hash_file = "../data/hash.txt"

# Hash
if os.path.exists(Hash_file):
	# File exists
	print("Hash file exists")
	read_file = open(Hash_file, "r")

	file = read_file.read()
	hash = get_hash_file(Excel_file)

	if(file == ""):
		# File is empty
		print("Hash file empty")
		run_analyze_file()
		write_hash_to_file(Hash_file)
		sys.exit()
		
	if(file == hash):
		print("Excel file not changed")
	else:
		print("Excel file changed")
		run_analyze_file()
		write_hash_to_file(Hash_file)

	read_file.close()
else:
	# File not exists
	print("Hash file not exists")
	run_analyze_file()
	write_hash_to_file(Hash_file)

print("Finished")
