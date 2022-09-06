def my_shiny_new_decorator(a_function_to_decorate):
    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def the_wrapper_around_the_original_function():
    
        # Put here the code you want to be executed BEFORE the original 
        # function is called
        print("Before the function runs")

        # Call the function from the parameter here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original 
        # function is called
        print("After the function runs")

    # At this point, `a_function_to_decorate` HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before
    # ...and after. It’s ready to use!
    return the_wrapper_around_the_original_function

def a_stand_alone_function():
    print("I am a stand alone function, don’t you dare modify me")

a_stand_alone_function() 
# Outputs: I am a stand alone function, don't you dare modify me

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()

# Outputs:
	# Before the function runs
	# I am a stand alone function, don't you dare modify me
	# After the function runs

a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
# Outputs:
	# Before the function runs
	# I am a stand alone function, don’t you dare modify me
	# After the function runs