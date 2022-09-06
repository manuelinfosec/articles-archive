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

print()
# ============ CELL 16 =============
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

print()
# ================= CELL 17 ===============
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