import unittest
from parse_csv import parse_csv

class ParseCsvTest(unittest.TestCase):

	def test_parse_csv(self):

		#Simple test case with 1 line and no special cases.
		self.assertTrue(parse_csv([["toan", "24", "male"]], "toan,24,male"))
		
		#Simple test case with 1 line and no special cases. #difference in age
		self.assertFalse(parse_csv([["toan", "24", "male"]], "toan,25,male")) 

		#Simple test case with 1 line with last line ending with '\r\n'
		self.assertTrue(parse_csv([["toan", "24", "male"]], "toan,24,male\r\n"))

		#Test with extra spaces at the beginning and the end of the field in csv Text
		self.assertTrue(parse_csv([["toan", "24", "male"]], "      toan         ,             24         ,male            \r\n"))

		#Test with two lines in csv Text
		self.assertTrue(parse_csv([["toan", "24", "male"], ["x", "20", "female"]],
		 "      toan         ,             24         ,male            \r\n  x, 20, female  "))

		#Test with four lines in csv Text
		self.assertTrue(parse_csv([["toan", "24", "male"], 
									["x", "20", "female"], 
									["y", "1", "gay"], 
									["z", "2", "les"]],
		 "      toan         ,             24         ,male            \r\n  x, 20, female  \r\ny,1,gay\r\nz,2,les"))


		#Test with fields contaning line-break and double-quote and commas
		self.assertTrue(parse_csv([["to \r\n an", "\"24, nguyen canh toan\"", "male"]], 
			"to \r\n an      ,      \"24, nguyen canh toan\"       ,       male               \r\n"))



if __name__ == '__main__':
	unittest.main()