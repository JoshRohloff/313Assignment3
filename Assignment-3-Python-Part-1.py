
#################################################################
## Assignment - 3 - part -1 (Python) ##
# Part-2 of the Assignment instructions can be found in the PDF
# document posted along with this file.
# Total Points: 40 points ##
# Name: type your name here
# Due Date: March 15 (Friday), 11.59 in Blackboard
# Type your answers in this python file.
#################################################################

###############
# Problem 1 ## (3 points)
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'

# 'o'

# 'djan'

# 'jan'

# 'go'

# Use indexing to reverse the string


###############
# Problem 2 ## (2 points)
###############

# Given this nested list:
l = [5, 7, [3, 5, 'hello', 8]]
# Reassign "hello" to be "goodbye"


###############
# Problem 3 ## (3 points)
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'greeting': 'hello'}

d2 = {'k1': {'k2': 'hello'}}

d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}


###############
# Problem 4 ## (2 points)
###############

# Use a set to find the unique values of the list below:
mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]


###############
# Problem 5 ## (3 points)
###############

# You are given two variables:
name = "Bob"
age = 20

# Use print formatting to print the following string:
"Hello my friend's name is Bob and he is 20 years old"


# Complete the tasks below by writing functions!

#####################
# -- PROBLEM 6 -- ## (3 points)
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    # CODE GOES HERE

    #####################
    # -- PROBLEM 7 -- ## (3 points)
    #####################

    # Given a string, return a new string made of every other character starting
    # with the first, so "Hello" yields "Hlo".

    # For example:

    # stringBits('Hello') → 'Hlo'
    # stringBits('Hi') → 'H'
    # stringBits('Heeololeo') → 'Hello'


def stringBits(str):
  # CODE GOES HERE

    #####################
    # -- PROBLEM 8 -- ## (4 points)
    #####################

    # Given two strings, return True if either of the strings appears at the very end
    # of the other string, ignoring upper/lower case differences (in other words, the
    # computation should not be "case sensitive").
    #
    # Note: s.lower() returns the lowercase version of a string.
    #
    # Examples:
    #
    # end_other('Hiabc', 'abc') → True
    # end_other('AbC', 'HiaBc') → True
    # end_other('abc', 'abXabc') → True


def end_other(a, b):
  # CODE GOES HERE

    #####################
    # -- PROBLEM 9 -- ## (4 points)
    #####################

    # Given a string, return a string where for every char in the original,
    # there are two chars.

    # doubleChar('The') → 'TThhee'
    # doubleChar('AAbb') → 'AAAAbbbb'
    # doubleChar('Hi-There') → 'HHii--TThheerree'


def doubleChar(str):
  # CODE GOES HERE

    #####################
    # -- PROBLEM 10 -- ## (6 points)
    #####################

    # Read this problem statement carefully!

    # Given 3 int values, a b c, return their sum. However, if any of the values is a
    # teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
    # and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
    # takes in an int value and returns that value fixed for the teen rule.
    #
    # In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
    # Define the helper below and at the same indent level as the main no_teen_sum().
    # Again, you will have two functions for this problem!
    #
    # Examples:
    #
    # no_teen_sum(1, 2, 3) → 6
    # no_teen_sum(2, 13, 1) → 3
    # no_teen_sum(2, 1, 14) → 3


def no_teen_sum(a, b, c):
  # CODE GOES HERE


def fix_teen(n):
  # CODE GOES HERE

    #####################
    # -- PROBLEM 11 -- ## (7 points)
    #####################

    # Implement a Python class called Employee. Every employee object will have three attributes: first name, last name, designation
    # Implement the getter and setter methods and the special method that returns the string representation of the object's data

    # Next create two employee objects with appropriate data and demonstrate at least one getter and and setter methods on these objects
