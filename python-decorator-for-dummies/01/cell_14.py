@my_shiny_new_decorator
def another_stand_alone_function():
    print("Leave me alone")

another_stand_alone_function()
# Outputs:  
	# Before the function runs
	# Leave me alone
	# After the function runs

another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)