import csv

def check_field(value, pos, csv):
	"""
	Check if the value matches the corresponding the next substring of
	input CSV string.
	
	params
	------
	value: string 
		the current element of the output.
	pos: int 
		the current position on the input CSV string.

	return: (boolean, int)
		True if matching is possible, False otherwise.
		The position for the checking of next element, -1 if the checking is done
	"""
	
	#elimination of space at the beginning of the field.
	while csv[pos] == ' ': 
		pos += 1

	#comparison 
	for it in value:
		if pos >= len(csv):
			return (False, -1)
		if it != csv[pos]:
			return (False, -1)
		pos += 1

	#elimination of space at the end of field.
	while pos < len(csv) and csv[pos] == ' ':
		pos += 1

	#check if the current field is the last field in csv
	if pos == len(csv):
		return (True, -1)

	if csv[pos] == ',':
		return (True, pos + 1)

	#check if the current field is the end of a line in csv	
	if pos < len(csv) -1 and csv[pos] == '\r' and csv[pos+1] == '\n':
		return (True, pos + 2)

	return (False, -1)

def parse_csv(result, csv):
	"""
	#Simple test case with 1 line and no special cases.
	>>> parse_csv([["toan", "24", "male"]], "toan,24,male")
	True
 
	#Simple test case with 1 line and no special cases. #difference in age
	>>> parse_csv([["toan", "24", "male"]], "toan,25,male")
	False

	#Simple test case with 1 line with last line ending with '\r\n'
	>>> sample = "toan,24,male\\r\\n"
	>>> parse_csv([["toan", "24", "male"]], sample )
	True

	#Test with extra spaces at the beginning and the end of the field in csv Text
	>>> parse_csv([["toan", "24", "male"]], "   toan     ,   24   , male   \\r\\n")
	True

	#Test with two lines in csv Text
	>>> parse_csv([["toan", "24", "male"], ["x", "20", "female"]],"  toan ,   24 ,male \\r\\n  x, 20, female  ")
	True

	#Test with four lines in csv Text
	>>> result = [["toan", "24", "male"], ["x", "20", "female"], ["y", "1", "gay"], ["z", "2", "les"]]
	>>> csv = "      toan         ,             24         ,male            \\r\\n  x, 20, female  \\r\\ny,1,gay\\r\\nz,2,les"
	>>> parse_csv(result, csv)
	True

	#Test with fields contaning line-break and double-quote and commas
	>>> result = [["\\"to \\r\\n an\\"", "\\"24, nguyen canh toan\\"", "male"]]
	>>> csv = "\\"to \\r\\n an\\",\\"24, nguyen canh toan\\",male"
	>>> parse_csv(result, csv)
	True

	"""
	pos = 0
	for line in result:
		for value in line:
			res, pos = check_field(value, pos, csv)
			if (res == False):
				return False
	return True


if __name__ == "__main__":

	import doctest
	doctest.testmod()
