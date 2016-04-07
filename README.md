# parse-csv

This is a simple guide for testing. I've included two testing modules of python. 

###* Doctest

Test cases are included in the function ``parse_csv`` within ``parse_csv.py`` already. 
To run use the command: 
	
  python parse_csv.py

If there is no notification(blankness) then all tests are passed.
For more details on each test, use the command 
	
	python parse_csv.py -v

Note that due to the nature of this testing module, all escape characters must be preceded by an additional
flash character ('\'). This causes a little bit messy for the input data, so I decided to include Unittest module.

###* Unittest

Test cases are included in ``parse_csv_test.py``
Compared to Doctest, Unittest has an disadvantage. There is no notifications (OK/not OK) for each test case.
If one test is not passed, then the programm immediately stops at that point.
Command for usage:
	
	python parse_csv_test.py

Choose whatever way of testing you prefer.
Thanks for spending time reading!
