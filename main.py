"""
Text type (String)
"""
# single line strings have a single or double quotation marks at the start and end of a string.

# s = "This is a single line string"
# print(s)
# print(type(s))

#========================================
# multline strings have triple single or triple double quotation marks at the start and end of a string.

# s = """ This is a multiline line 
# string example"""
# print(s)

#========================================
# The .title() method turns the first letter of each word in a string from a lowercase to a uppercase letter.

# name = "michael jordan"
# name2 = "kobe"
# print(name.title())
# print(name2.title())

#========================================
# The .upper() method turns all letters in a string from lowercase to uppercase letters whilst the .lower() method does the opposite.

# name = "michael jordan"
# name2 = "KEVIN DURANT"
# print(name.upper())
# print(name2.lower())

#========================================
# This is an f string, it allows you to put variables into a string.

# firstName = "lebron"
# lastName = "james"
# fullName = f"{firstName} {lastName}"
# print(fullName)

#========================================
# \t at the start of string is used to add a tab to the Text

# name = "\tpython"
# print(name)

#========================================

# \n in a string at the start of a new world puts words on a new line.

# sports = "\nbasketball\nboxing\nmma"
# print(sports)

#========================================

# using \n\t creates string on new line and also causes the new line to start with a tab. tabs, spaces and newlines are refered to whitespaces in python.

# sports = "\n\tbasketball\n\tboxing\n\tmma"
# print(sports)

#========================================
# the .strip() method reomves all whitespaces(spaces) in a string, using .rstrip() just removes all whitespaces(spaces) on the right side of a string whilst .lstrip() does the opposite.

# sport = "    basketball   "
# sport2 = "    boxing   "
# sport3 = "    tennis   "
# print(sport.rstrip())
# print(sport2.strip())
# print(sport3.lstrip())

# ========================================

# when using a string with an aptostrophe, use a double, triple single, triple double quotation marks to start and end a string to avoid any syntax errors.

# error
# print('They're a really athletic team')

# correct ways
# print("They're really playful husky puppies")
# print("""The dog's name was hulk""")
# print('''The cat's name was skylar''')

#========================================

# find a characater by index

# s = "string sample"
# print(s[5])

# slicing
# s = "string sample"
# print(s[1:6])

#========================================

# a string is immutable

# s = "string sample"
# s[2] = "o"
# print(s)

"""
Numeric type (Integer, Float, Complex)
"""
# You can add a integer or float using a +, subtract a integer or float using a -, multiply a integer or float using a *, exponent a integer or float using a ** and divide a integer or float using a /. 

# print(4+4)
# print(16-8)
# print(4*2)
# print(2**3)
# print(16/2)

#========================================


# Integer
# inegers are immutable
# x = 234567324734743
# print(type(x))

# Float
# # accurate up to 15-16 decimal places
# x = 0.3763587356734348474674865958596
# print(type(x))
# print(x)

# complex
# x = 1 + 2j
# print(type(x))

#========================================


# assigning a variable to a value, then printing a message out that includes that variable.

# age = 23
# print(f"I'm age {age} years old")


#========================================

# you can use underscore a _ in intergers and floats, especially when dealing with long numerical values. For example, if wanted to assign the value £1000000 to variable, you can write it as shown below:

# a_million_pounds = 1_000_000.0
# a_million_pounds2 = 1_00_00_00
# a_million3 = 1_00_000_0
# print(a_million_pounds)
# print(a_million_pounds2)
# print(a_million3)

#========================================

# dividing two intergers returns their answer as a float e.g.

# print(4/2)

# also adding, subtracting. multiplying, dividing or exopenting a integer and float number always returns result as a float value e.g.

# print(8.0/2)
# print(2.0+2)
# print(12.0-8)
# print(2*2.0)
# print(2.0**2)

#========================================

# a CONSTANT is a variable, that has a value that never changes throught the life of a python program, meaning the value is stays constant. For variable to be constant, all its letters need to be in capital letters e.g.

# THIS_IS_A_CONSTANT_EXAMPLE1 = 23

#========================================

# A comment is a way for  python programmers to make notes without it being printed out in the terminal or being ignored by python. A comment alwsys starts with a hash mark = #.

#========================================

# the zen of python is brief set of principles for writing good code in python. to get the zen of python just type:

# import this


"""
Sequence type (List, Tuple, Range)
"""

# list =[]
# A list is mutable
# homogeneous


# x = [10, 11, 12]
# print(x[2])
# print(x[1:3])
# x[2] = 18
# print(x)

# tuple
# # heterogenous
# tuple = ()


# tuple = ("cat", [4,3,2], (1,2,3))
# print(tuple)


#========================================

# both examples below are types of tuple, without commas makes it a string.

# tuple = "hello", 
# tuple = ("hello",)
# print(type(tuple))

#========================================

# tuple = ("cat", [4,3,2], (1,2,3))
# print(tuple[1])
# print(type((1,2,3)))

#========================================

# tuple is immutable

# tuple = ("cat", [4,3,2], (1,2,3))
# tuple[0] = "mat"
# print(tuple)

#========================================

# range

# x = range(30)
# for n in x:
#    print(n)
# print(type(x))
  

"""
Mapping types (Dictonairy)
"""

# x = {}
# print(type(x))

#========================================

# dictionairy is mutable
# dictionairy = {}, also when empty

# x = {"name" : "Jordan", "age": 24, "goal" : "money"}
# print(x["age"])
# print(x["name"])
# print(x.get("goal"))
# x["age"] = 23
# print(x)

"""
Set types
"""
# set = {}, the same brackets used for dictionairy however set only uses single values
# set = set(), when empty



# x = {1, 2, "money"}
# print(x)
# print(type(set))

#========================================
# set supports mixed data tupe but their all immutable. set dosen't allow indexing or slicing.
# even a list inside a set is immutable, can't have a mutable [list] in {set}
# set dosent allow duplicate variable it will remove extre copies when printed e.g. {2,1,2} will be {2,1} when printed.


"""
BooLean type (true or false)
"""
# True is equal to 1 & false is equal to 0.



# print(type(True))

# booLean as numbers
# print(True == 1)
# print(False == 0)

# interesting logic 
# print(True + True) 
# print (False + False) 

# not boolean operater
# print(not True)
# print(not False)

# and boolean operateor 
# print(True and False) = False
# print(True and True) = True
# print(False and False) = False

# or boolean operator
# print(True or False) = True
# print(True or True) = True
# print(False or False) = Fasle


