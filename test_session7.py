import pytest
import random
import string
import session7
import os
import inspect
import re
import math
import time
from session7 import return_closure
from session7 import ret_closure_fibonacci
from session7 import ret_closure_global_list
from session7 import ret_closure_local_list


############################## Generic test cases ###########################

def test_session7_readme_exists():
    """ This function is to test wether a README.md file exists. If it doesn't
        then an error will be raised.
    """
    assert os.path.isfile("README.md"), "README.md file missing!"



def test_session7_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
    significant indenting
    """
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 







############################## Tests for function "return_closure" ###########################

def test_session7_check_docstring_exists():
	""" The test passes if closure returns False since length of doctring in abc is < 50 chars
	"""	
	def abc():
		pass
	with pytest.raises(TypeError, match=r".*The input function does not contain a docstring*"):
		session7.return_closure(abc)()


def test_session7_check_docstring_less_chars():
	""" The test passes if closure returns False since length of doctring in abc is < 50 chars
	"""	
	def abc():
		"""Hello world"""
		pass
	assert session7.return_closure(abc)() == False, "Function abc() has docstring of less than 50 chars"


def test_session7_check_docstring_more_chars():
	""" The test passes if closure returns True since length of doctring in abc is > 50 chars
	"""	
	def abc():
		"""Hello world, Hello world, Hello world, Hello world, Hello world, Hello world, Hello world, Hello world, 
    	Hello world, Hello world, Hello world, Hello world, Hello world, Hello world, Hello world, Hello world, """
		pass
	assert session7.return_closure(abc)() == True, "Function abc() has docstring of less than 50 chars"


def test_session7_check_docstring_length_5_chars():
	""" The test passes if closure returns True since length of doctring in abc is < 50 chars AND we are passing input length as 5 chars
	"""	
	def abc():
		"""Hello world"""
		pass
	assert session7.return_closure(abc, length = 5)() == True, "Function abc() has docstring of less than 50 chars"


def test_session7_check_empty_docstring():
	""" The test passes if closure returns False since length of doctring in abc is 0 AND we are passing input length as 5 chars
	"""	
	def abc():
		""""""
		pass
	assert session7.return_closure(abc, length = 5)() == False, "Function abc() has docstring of less than 50 chars"










####################### Validations for ret_closure_fibonacci function #################################

def test_session7_fibonacci_output():
	""" The test passes if closure returns tuple of fibonacci numbers 3,5,8,13,21
	"""	
	fibonacci = session7.ret_closure_fibonacci()
	assert (fibonacci(), fibonacci(), fibonacci(), fibonacci(), fibonacci()) == (3,5,8,13,21), "ret_closure_fibonacci() isn't working as expected"


def test_session7_fibonacci_input_start():
	""" The test passes if closure returns tuple of fibonacci numbers 8,13,21,34,55
	"""	
	fibonacci = session7.ret_closure_fibonacci( last_two = [3,5] )
	assert (fibonacci(), fibonacci(), fibonacci(), fibonacci(), fibonacci()) == (8,13,21,34,55), "ret_closure_fibonacci() isn't working as expected"












####################### Validations for ret_closure_global_list function #################################

def test_session7_ret_global_dict_oput():
	""" The test passes if closure returns a global dict of function name and count of executions
	"""	
	def add (a,b):
		return a+b
	def mult(a,b):
		return a*b

	add  = session7.ret_closure_global_list(add)
	mult = session7.ret_closure_global_list(mult)

	for i in range(10):
		add(i, i+1)
	for i in range(10):
		mult(i, i+1)

	assert session7.global_dict_fn_cnt == {'add': 10, 'mult': 10}, "ret_closure_global_list not working properly"












	####################### Validations for ret_closure_local_list function #################################

def test_session7_ret_local_dict_oput():
	""" The test passes if closure returns a local dict of function name and count of executions
	"""	
	def add (a,b):
		return a+b
	def mult(a,b):
		return a*b

	add_counter = dict()
	add = session7.ret_closure_local_list(add, add_counter)
	mult_counter = dict()
	mult = session7.ret_closure_local_list(mult, mult_counter)

	for i in range(10):
		add(i, i+1)
	for i in range(10):
		mult(i, i+1)

	assert add_counter == {'add': 10}, "ret_closure_local_list not working properly"
	assert mult_counter == {'mult': 10}, "ret_closure_local_list not working properly"




def test_session7_ret_local_common_dict():
	""" The test passes if closure returns a local dict of function name and count of executions
	"""	
	def add (a,b):
		return a+b
	def mult(a,b):
		return a*b

	add_counter = dict()
	add = session7.ret_closure_local_list(add, add_counter)
	mult = session7.ret_closure_local_list(mult, add_counter)

	for i in range(10):
		add(i, i+1)
	for i in range(10):
		mult(i, i+1)

	assert add_counter == {'add': 10, 'mult': 10}, "ret_closure_local_list not working properly"