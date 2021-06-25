#
#AGENDA
#------
#This file contains the description of 5 functions.
#
#
#For each function, the description follows this structure:
#
#a. Its purpose.
#b. Arguments
#c. Functionality




1. squared_power_list(number, args, start=0, end=5, kwargs)

	a. Its purpose
	   -----------
	   This function is used to calculate the powers of an input number.

	b. Arguments
	   ---------
	   This function takes 5 arguments (number, args, start=0, end=5, kwargs)
	   First argument is the number for which power will be computed.
	   Second argument consumes any number of positional arguments passed to this function.
	   Third argument is the first power that will be computed.
	   Fourth argument is the last power that will be computed.
	   Fifth argument is a dynamic argument to take a dictionary of keyword arguments.

	c. Functionality
	   -------------
	   If the start power is 1 and end is 4, then this function will compute powers as: n**1, n**2, n**3, n**4








2. polygon_area (length, args, sides = 3, kwargs)

	a. Its purpose
	   -----------
	   This function is used to calculate the area of an input polygon

	b. Arguments
	   ---------
	   This function takes 4 arguments (length, args, sides = 3, kwargs)
	   First argument is the length of the side of polygon
	   Second argument consumes any number of positional arguments passed to this function.
	   Third argument is the number of sides of the polygon, default is 3, i.e., a triangle.
	   Fourth argument is a dynamic argument to take a dictionary of keyword arguments.

	c. Functionality
	   -------------
	   The function computes the area of a polygon using the formula, Area of a polygon = (perimeter x apothem)/2








3. temp_converter(temp, args, temp_given_in = 'f', kwargs)

	a. Its purpose
	   -----------
	   This function is used to convert the temprature from celsius to farhenheit and vice versa.

	b. Arguments
	   ---------
	   This function takes 4 arguments (temp, args, temp_given_in = 'f', kwargs)
	   First argument is the temprature value.
	   Second argument consumes any number of positional arguments passed to this function.
	   Third argument is the type of input value, celsius or farhenheit
	   Fourth argument is a dynamic argument to take a dictionary of keyword arguments.

	c. Functionality
	   -------------
	   This function is used to convert the temprature from celsius to farhenheit and vice versa.








4. speed_converter (speed, args, dist='km', time='min', kwargs)

	a. Its purpose
	   -----------
	   This function is used to convert the input speed (in KM/HR) into a speed of different units.

	b. Arguments
	   ---------
	   This function takes 5 arguments (speed, args, dist='km', time='min', kwargs)
	   First argument is the speed value.
	   Second argument consumes any number of positional arguments passed to this function.
	   Third argument is the unit of distance.
	   Fourth argument is the unit of time.
	   Fifth argument is a dynamic argument to take a dictionary of keyword arguments.

	c. Functionality
	   -------------
	   This function is used to convert the input speed (in KM/HR) into a speed of different units.



5. time_it(fn, *args, repetitions= 1, **kwargs)

	a. Its purpose
	   -----------
	   This function is used to time 'n' repretition of the function passed as parameter to ths function.

	b. Arguments
	   ---------
	   This function takes 4 arguments (fn, args, repetitions= 1, kwargs)
	   First argument is the function that will be timed.
	   Second argument consumes any number of positional arguments passed to this function.
	   Third argument is a named argument with the default value of 1.
	   Fourth argument is a dynamic argument to take a dictionary of keyword arguments.

	c. Functionality
	   -------------
	   It times the execution of the passed input function and returns a list that contains time of execution in each repeatition.





