# Purpose of this project
This project contains the functions to decide the winner of a poker game. Following functions are defined

# return_closure
This function returns a closure tha checks  the length of docstring in the input function. It also ensures that the function
contains a docstring.

# ret_closure_fibonacci
This function takes a keyword argument of last-two fibonacci numbers (if not passed, it defaults to [1,2]).
It then returms a closure which when executed, returns the next fibonacci number.

# ret_closure_global_list
This function takes a function as input and returns a closure which holds a global dictionary free variable.
The free variable stores the number of executions of the input function. If this function is called 3 times
one each for a different input function, then we will get 3 different closures all referring to the same
global dictionary free variable.

# ret_closure_local_list
This function takes a function and a dictionary as input and returns a closure which holds a nonlocal dictionary free variable.
The free variable stores the number of executions of the input function. If this function is called 3 times, each with a different function
and dictioary variable, then we will get 3 different closures all referring to a separate cnonlocal dictionary free variable.
