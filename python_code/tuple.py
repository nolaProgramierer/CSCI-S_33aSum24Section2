# Tuples
# A tuple is sequence of values, of any type, that are immutable
# Tuples are written with round brackets.


print("1)")
# Instantiate a tuple
t1 = ('a', 'b', 'c', 'd', 'e')
print(t1)


print()
print("2)")
# One value of tuples is their ability to return multiple values.
# divmod is a built-in function that take two arguments and 
# returns a tuple of 2 values


result = divmod(101, 50)
print(result)


print()
print("3)")
# also you can assign the result to different values

quotient, result1 = divmod(101 , 50)
print(quotient)
print(result1)


print()
print("4)")
# Using min and max methods, which are built-in functions
# that find the smallest and largest numbers of a sequence

# Return a tuple
def find_biggest_smallest(result):
    return min(result), max(result)

r = find_biggest_smallest(result)
print(r)

#---------------------------------------------------
# Packing & Unpacking

# Packing in Python generally refers to collecting multiple values 
# into a single variable, typically using tuples, lists, or 
# dictionaries. This is useful for various operations like 
# returning multiple values from a function or passing a 
# variable number of arguments to a function.

print()
print("5)")
# 5)
# Packing
piano = ("Yamaha", "Glossy Black", 3500)

# Unpacking
brand, finish, price = piano

print(f"Brand: {brand}, Finish: {finish}, Price: ${price}")

print()
print("6)")
#6)
# Packing position arguments
def display_piano_details(brand, finish, price):
    print(f"Brand: {brand}, Finish: {finish}, Price: ${price}")

piano_details = ("Yamaha", "Glossy Black", 3500)

# Unpacking the tuple into function arguments
display_piano_details(*piano_details)


print()
print("7)")
#7) Packing keyword arguments
def display_piano_details(brand, finish, price):
    print(f"Brand: {brand}, Finish: {finish}, Price: ${price}")

piano_details = {"brand": "Yamaha", "finish": "Glossy Black", "price": 3500}

# Unpacking the dictionary into function arguments
display_piano_details(**piano_details)

print()
print("8)")
#8)
#Sum a tuple
t3 = (1, 2, 3, 4)
print(sum(t3))

  