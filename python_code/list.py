a = [1, 2, 3]
b = [4, 5, 6]

composers = ["Beethoven", "Ravel", "Brahms", "Debussy", "Mahler", "Bruckner", "Mozart", "Bach", "Stravinsky"]

cars = [
    {"brand": "BMW", "trim": "328i", "color": "gray", "price": 38900},
     {"brand": "Mercedes", "trim": "350E", "color": "white", "price": 89000},
      {"brand": "Porsche", "trim": "911", "color": "orange", "price": 95000},
       {"brand": "Kia", "trim": "Sorento", "color": "blue", "price": 30900},
        {"brand": "Toyota", "trim": "Sienna", "color": "gray", "price": 51200},
]

print("1")
# 1) Length
l = len(composers)
print(l)

print()
print("2")
# 2) Concatenation
c = a + b
print(c)

print()
print("3")
# 3) Make a list
# Note double brackets
my_faves = list(("Steinway","Bösendorfer", "Bechstein"))
my_faves1 =["Steinway","Bösendorfer", "Bechstein"]
print(my_faves)
print(my_faves1)

print()
print("4")
# 4) Add to a list
my_faves.append("Baldwin")
print(my_faves)

print()
print("5")
# 5) Slice
# It is a technique used to extract a portion of a sequence, such as a list, 
# tuple, or string. Slices are created by specifying a start (inclusive), stop ()
# (exclusive), and optional step value within square brackets, 
# separated by colons (:). 

# Return a list with Ravel & Brahms
# Start on index 1 and end on index 3 (excluding it)
s = composers[1:3]
# Return a list with Beethoven, Ravel, Brahms, Debussy, & Mahler
# Start on index 0 and stop on index 5 (excluding it) 
s1 = composers[:5]
# Return a list with Mozart, Bach, & Stravinsky
# Start on index 6 and go until end
s2 = composers[6:]
# Return a list with Ravel and Debussy
# Start on index 1, go to index 4 (excluding it), incrementing by 2
s3 = composers[1:4:2]
# Return a list in reverse order
#Incrementing the index everytime by -1 (reversing the iterable)
s4 = composers[::-1]
# Return Bach and Mozart
s5 = composers[-3:-1]
print(s)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

print()
print("6")
# 6) Split
# The split() method in Python is used to break a string 
# into a list of substrings based on a specified delimiter. 
# If no delimiter is specified, the method splits the string 
# at whitespace by default. It returns a list of substrings.

# Break a string into word
my_str = "I love working in python!"
my_str1 = "L-O-L"
str_list = my_str.split()
str_list1 = my_str1.split("-")
print(str_list)
print(str_list1)

print()
print("7")
# 7) Traversing a list
def list_composers(l):
    for item in l:
        print(item)
list_composers(composers)

print()
print("8")
# 8) Traversing a list of objects
def show_objs(objArr):
    for obj in objArr:
        print(obj)
show_objs(cars)

print()
print("9")
# 9) Adding up element in a list
total = sum(b)
print(total)

print()
print("10")
# 10) Return a list of the composers, but lower case
def to_lower_case(comps):
    result = []
    for comp in comps:
        result.append(comp.lower())
    return result
print(to_lower_case(composers))

print()
print("11")
# 11) Return a list of the composers that being with the letter 'b'
def composers_with_b(comps):
    result = []
    for comp in comps:
        if comp[0] == "B":
            result.append(comp)
    return result
print(composers_with_b(composers))





