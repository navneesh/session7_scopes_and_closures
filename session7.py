"""WRITE PROPER ASSINGMENT DESCIPTION HERE AND DELETE THIS MESSAGE"""

import time
import math

def return_closure(fn, length = 50):
	"""This function returns a closure that utilizes the nonlocal variable 'length' to check if the doctring in input function has chars > length"""
	def closure_func():
		
		# Raise an error if the function does not contain a docstrong
		if fn.__doc__ is None:
			raise TypeError("The input function does not contain a docstring")
		return True if len(fn.__doc__) > length else False
	return closure_func




def ret_closure_fibonacci(last_two=[1,2]):
	"""This function returns a closure that utilizes the nonlocal variable 'last_two' and return the next fibonaccinumber"""
	# print(last_two)
	def fibonacci():
		nonlocal last_two
		next_fibonacci = sum(last_two)
		last_two[0], last_two[1] = last_two[1], next_fibonacci
		# print(next_fibonacci)
		# print(last_two)
		return next_fibonacci
	return fibonacci




global_dict_fn_cnt = dict()

def ret_closure_global_list(fn):
	"""This function returns a closure that utilizes the gloal variable 'global_dict_fn_cnt' to record the executions of function passed as input to this function"""
	# initializing a counter
	count = 0
	def closure_func(*args, **kwargs):
		# reference to nonlocal variable that we intend to change
		nonlocal count
		count = count + 1
		# global dictionary inserted/updated with latest count of "fn" function
		global_dict_fn_cnt[fn.__name__] = count
		# returning output as the original "fn" would have returned
		return fn(*args, **kwargs)
	# returning a closure which enhances functionality of "fn" by also maintaining its execution count
	return closure_func








def ret_closure_local_list(fn, my_dict):
	"""This function returns a closure that utilizes the nonlocal dict variable 'my_dict' to record the executions of function passed as input to this function"""
	# initializing a counter
	count = 0
	def closure_func(*args, **kwargs):
		# reference to nonlocal variable that we intend to change
		nonlocal count
		nonlocal my_dict
		count = count + 1
		# global dictionary inserted/updated with latest count of "fn" function
		my_dict[fn.__name__] = count
		# returning output as the original "fn" would have returned
		return fn(*args, **kwargs)
	# returning a closure which enhances functionality of "fn" by also maintaining its execution count
	return closure_func

