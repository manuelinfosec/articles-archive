Get the full experience reading this article on [Medium](https://manuelinfosec.medium.com/python-decorators-for-dummies-c58cdd78cf6b)
<br><br>

# Python Decorators For Dummies
## Part One: The Best Explanation You Can Find

Hey reader,

Before we get on with this article, I want to assume you're coming from a basic background in Python. If not, make sure you understand the following concepts in Python programming before hoping further:

- Python Functions.
- Python Exceptions & Error handling,

If you're not new to Python, you should have come across code like this: 

```python
import discord
client = discord.Client(intents=intents)

@client.event # take note of this line
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event # take note of this line
async def on_message(msg):
    if msg.content == "":
        pass
	...
```

For a little story behind the preceding code, I was creating an automation bot for Discord using the [discord.py](https://discordpy.readthedocs.io/) library and a colleague approached me while coding. With not so much experience in the Python language, she asked about the lines highlighted with comments above. Basically, those are Python Decorators. I was obliged to explain to her the concept of decorators in Python, and like ever other interested learner, that one gesture of curiosity led to many more queries and questions. 

Although I tried my possible best to put her through, it was more than I could explain at one shot. One of the questions that I couldn't answer enough was, **"Can Python decorators be chained? If yes, how?"**. This got stuck with me, and I thought it was a good idea to explain such to the and so many others, on Medium, the beautiful concept of **Function Decorators**.

<img src="https://github.com/manuelinfosec/articles-archive/blob/main/python-decorator-for-dummies/01/images/article-banner.png" alt="Article banner">

This article aims at introducing Python decorators to you and putting an end to her curiosity. If you'll be involved in the exercises in this article , I recommend you use a Jupyter Notebook for the ease of managing various code chunks.

If you've not, drop a follow on any of my various social handles to get notified when I make new article alerts:
-   [Twitter](https://twitter.com/manuelinfosec),
-   [Facebook](http://facebook.com/manuelinfosec),
-   [YouTube](http://m.youtube.com/ManuelInfoSec).

## Decorator Basics
### Python's Function as objects
Decorators allow you to inject or modify code in functions or classes. To understand decorators, you must first understand that functions are objects in Python. This has important consequences. Let’s see why with a simple example:

```python
def shout(word='yes'):
    return word.capitalize() + '!'

print shout()
# outputs : 'Yes!'
```

As an object, you can assign the function to a variable like any other object. Let's do so in another cell.

```python
scream = shout
```

Notice we don't use parentheses; we are not calling the function, we are putting the function `shout` into the variable `scream`. It means you can then call `shout` from `scream`. Like below.

```python
print scream()
# outputs : 'Yes!'
```

More than that, it means you can remove the old name `shout`, and the function will still be accessible from `scream`.

```python
# deleting the shout() object
del shout

try:
	# trying to access the deleted shout() object
    print(shout())
except NameError as e:
    print(e)
    #outputs: "name 'shout' is not defined"

print(scream())
# Outputs: 'Yes!'
```

As expected! Keep in mind that we'll circle back to this shortly. Another interesting property of Python functions is they can be defined... inside another function!

```python
def talk():
    # Defining a function on the fly in `talk` ...
    def whisper(word='yes'):
        return word.lower() + '...'
    # ... and using it right away!
    print(whisper())

talk()
# Outputs: "yes..."
```

You call `talk`, that defines `whisper` EVERY TIME you call it, then `whisper` is called in `talk`.  But `whisper` DOES NOT EXIST outside `talk` as illustrated below:

```python
try:
    print(whisper())
except NameError as e:
    print(e)
    #outputs : "name 'whisper' is not defined"
```

I don't know about you but this proves to me that Python's functions are objects and like every object they exist within a scope. Beyond that scope, they're non-existent.

### Functions' Reference
Still here? Here's the fun part... Now that you've seen that functions are indeed objects in Python. Therefore, functions: 
- can be assigned to variable,
- can be defined in another function.

That means that **a functions can return another function**. Have a look:

```python
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
```

In the condition, we are not calling the function, hereby, no `()` parentheses; instead, we’re returning the function object. How does this make sense then? Let me show you.

```python
# Get the function and assign it to a variable
talk = getTalk()     

# You can see that `talk` is here a function object:
print(talk)
# Outputs : <function shout at 0xc1d2859b>

# The object is the one returned by the function:
print talk()
# Outputs: Yes!

# And you can even use it directly if you feel wild:
print(getTalk('whisper')())
# Outputs: yes...
```

But wait...there’s more! If you can `return` a function, then you should be able to pass one as a parameter. In your notebook, make reference to `scream` in the next cell.

```python
def doSomethingBefore(func): 
    print("I do something before then I call the function you gave me")
    print(func())

doSomethingBefore(scream)
# Outputs: 
	# I do something before then I call the function you gave me
	#Yes!
```

Well, this is all needed to understand decorators. You see, decorators are "wrappers", which means that **they let you execute code before and after the function that decorate** without modifying the function itself.

### Decorators: The Naive Way
Before we continue, let us define a decorator in my own terms:

		A decorator is a function that expects ANOTHER functions as parameter.

Here's how you'd create a decorator without using the Python's way of declaring decorators. If that confuses you, I meant the manual way:

```python
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
```

We have just created a decorator for future functions. Now, imagine you create a function that you don't want to ever touch again:

```python
def a_stand_alone_function():
    print("I am a stand alone function, don’t you dare modify me")

a_stand_alone_function() 
# Outputs: I am a stand alone function, don't you dare modify me
```

Well, you can decorate it to it extend its behaviour. Just pass it to the decorator created in the previous cell, it will wrap it dynamically in any code you want and return you a new function ready to be used:

```python
a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()

# Outputs:
	# Before the function runs
	# I am a stand alone function, don't you dare modify me
	# After the function runs
```

Now, you probably want that every time you call `a_stand_alone_function`, `a_stand_alone_function_decorated` is called instead. That’s easy, just overwrite `a_stand_alone_function` with the function returned by `my_shiny_new_decorator` like this:

```python
a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
# Outputs:
	# Before the function runs
	# I am a stand alone function, don’t you dare modify me
	# After the function runs
```

And guess what? That’s EXACTLY what decorators do!

### Decorators Demystifying
The previous example, using the decorator syntax:

```python
@my_shiny_new_decorator
def another_stand_alone_function():
    print("Leave me alone")

another_stand_alone_function()
# Outputs:  
	# Before the function runs
	# Leave me alone
	# After the function runs
```

Yes, that's all. It's that simple. `@decorator` is just a shortcut to:

```python
another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)
```

Decorators are just a Pythonic variant of the [decorator design pattern](http://en.wikipedia.org/wiki/Decorator_pattern). There are several classic design patterns embedded in Python to ease development (like iterators).

Over to the initial question of the day, you can accumulate decorators. This is how it is done the naive (manual) way:

```python
def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper

def sandwich(food='--ham--'):
    print(food)

sandwich()
# Outputs: --ham--

sandwich = bread(ingredients(sandwich))
# sandwich is now reference to the decorator
# instead of the `--ham` string.
sandwich()

# Outputs:
	# </''''''\>
	# #tomatoes#
	# --ham--
	# ~salad~
	# <\______/>
```

For a rundown for what happens in the code above.

At the base of it all, `sandwich()` returns a string "--ham--". This same function is passed as argument to a decorator, `ingredients()`. Printing operations before and after furthermore, returning the `sandwich` function (as an object) ready to be decorated again. The last decorator, `bread()` which still accepts a function as parameter, does the same as `ingredients()` and performs printing operations before and after the `sandwich` object. From this point, you can retrace the steps and this will paint a better picture in the mind.

Let's make this easier, using the Python decorator syntax:

```python
@bread
@ingredients
def sandwich(food="--ham--"):
	print(food)

sandwich()

# Outputs:
	#</''''''\>
	# #tomatoes#
	# --ham--
	# ~salad~
	#<\______/>
```

It is worth noting that the order you set the decorators MATTERS:

```python
@ingredients
@bread
def strange_sandwich(food='--ham--'):
    print(food)

strange_sandwich()
# Outputs:
	##tomatoes#
	#</''''''\>
	# --ham--
	#<\______/>
	# ~salad~
```

I intend to keep this article short and concise, so we'll end here for today. In the next article, we'll easily answer the question of the day and also take decorators to the next level where we'll see some advanced uses of decorators in Python.

Below is a notebook with containing all the code used for this exercise:

<iframe src="https://gist.github.com/manuelinfosec/5ac21010241545d4aca77d6dc70e3368/">
</iframe>


### Conclusion
Did you enjoy this introductory article? How simple was it? Tell me in the comments. 

You started this tutorial by looking a little closer at functions, particularly how they can be used beyond the scope of other functions and the limits outside of their scope. Then you learnt, about decorators in both (naive and Pythonic) ways such that:
- They can be reused,
- They can decorate functions with arguments and return values,
- ..etc.

This is more than enough for an introduction to Python decorators. See you in the next article.

*Signing out,*
*Manuel.*