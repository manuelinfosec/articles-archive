def getTalk(kind='shout'):
    # We define functions on the fly
    def shout(word='yes'):
        return word.capitalize() + '!'

    def whisper(word='yes'):
        return word.lower() + '...'

    # Then we return one of them
    if kind == 'shout':
	    # What happened here?
        return shout  
    else:
        return whisper

# Get the function and assign it to a variable
talk = getTalk()     

# You can see that `talk` is here a function object:
print(talk)
# Outputs : <function shout at 0xc1d2859b>

# The object is the one returned by the function:
print(talk())
# Outputs: Yes!

# And you can even use it directly if you feel wild:
print(getTalk('whisper')())
# Outputs: yes...