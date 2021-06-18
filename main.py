"""
Text type (String)
"""

# s = "This is a single line string"
# print(s)
# print(type(s))

#========================================

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


