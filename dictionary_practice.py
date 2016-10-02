grocery_list = {"apples": 2, "oranges": 3, "bananas": 5, "grapes": 4, "milk": 1}

# check to see if grocery_list carries pies.
# if so, print the number of pies it carries
# else print False
print grocery_list.get("pies", False)

# print all the keys in a list
print grocery_list.keys()

# print all the values in a list
print grocery_list.values()

for item, quantity in grocery_list.items():
    print "I have %d %s in my shopping cart." % (quantity, item)

# print a list of the keys sorted alphabetically
print sorted(grocery_list)

# prints a list of tuples sorted by key values numerically ascending
print sorted(grocery_list.items(), key = lambda(a, b): b)

# prints a list of tuples sorted by key values numerically descending
# because we set reverse to True
print sorted(grocery_list.items(), key = lambda(a, b): b, reverse=True)
