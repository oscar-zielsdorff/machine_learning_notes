# Run 'python3 -i script.py' to interact with the file.

## Importing libraries (modules) ##########################################
import math 
import math as mt # allows calling by custom name
from math import * # allows directly calling defined variables/functions

# Three useful functions for helping understand things:
import numpy
type(numpy.random) # submodule of numpy
dir(numpy) # lists functions and attributes
# help(numpy)

## Functions #############################################################
# Docstrings allow showing a message when help() is used.
# Default values can be assigned to parameters.
def greetings(name='Oz'):
    '''
    Prints a message to the screen for the specified person.

    >>> greetings()
    Hello, Oz

    >>> greetings("Calvin")
    Hello, Calvin
    '''

    print('Hello, ' + name)

# Passing a function as an argument.
def pass_func_as_arg():
    print(
        'The number with the largest absolute value is',
        max(1, -5, -9001, 9000, key=abs)
    )

## Bools and Conditionals ###############################################
# Order of operations for booleans.
# and is evaluated before or.
True or True and False # True
(True or True) and False # False

# Some types can be converted into bools.
bool('') # Empty strings are False
bool('qwerty') # Other strings are True
bool(0) # Zero is False
bool(-1) # Any other number is True
bool([]) # Empty lists are False
bool([0]) # Lists with values are True
bool(()) # Empty tuples are false
bool((0,)) # Tuples with values are True

# Some conditionals work a single line
def concise_is_negative(number):
    return True if number < 0 else False

def did_you_hear_something(scared=True):
    print(
        'There is',
        'nothing' if scared else 'something',
        'out there'
    )

# Standard syntax
if False:
    pass
elif False:
    pass
else:
    pass

## Lists (mutable) ######################################################
planets = [
    'mercury', 'venus', 'earth',
    'mars', 'jupiter', 'saturn',
    'uranus', 'neptune',
]
len(planets) # 8
sorted(planets) # returns in alphabetical order
# sum(num_list)
# max(num_list)

# Can be accessed from the end using negative numbers
planets[-1] # neptune

# Can be sliced
planets[0:3] # mercury, venus, earth (last index exclusive)
planets[:3] # mercury, venus, earth (assumed start)
planets[6:] # uranus, neptune (assumed length of list)
planets[1:-1] # all planets except first and last
planets[-3:] # last 3 planets

# Can be specifically assigned
planets[0] = 'hydrargyros'
planets[1:3] = ['aphrodite', 'gaia']
planets[:3] = ['mercury', 'venus', 'earth']

# Can add/remove values
planets.append('pluto')
planets.pop()

# Can be searched or checked
planets.index('earth') # 2
'pluto' in planets # False

## List Comprehensions ###################################################
def list_comp_examples():
    squares = [n**2 for n in range(10)]
    print('squares:', squares)

    short_planets = [
        planet.upper() + '!' 
        for planet in planets if len(planet) < 6
    ]
    print('short planets:', short_planets)

## Tuples (immutable) ####################################################
t = (1, 2, 3)
t = 1, 2, 3 # same result

# often used for functions with multiple return values.
x = 0.125
x.as_integer_ratio() # (1,8) representing fraction
numerator, denominator = x.as_integer_ratio() # assign tuple values

## Loops #################################################################
def loop_examples():
    # for loops
    for planet in planets:
        print(planet, end=' ') # print all on same line
    print()

    for i in range(5): # Iterates 5 times
        print("Doing important work. i =", i)

    # while loops
    while i < 10:
        print(i, end=' ')
        i += 1

## Strings ###############################################################
def string_examples():
    # triple quotes count newlines and tabs
    print('''Hello from above
hello from below
    hello from slightly to the right''')

    # strings are immutable
    # str[0] = 't' # results in error

    # strings indexed like lists
    str = 'The big bang'
    print(str[0]) # T
    print(str[-4:]) # bang
    print(str.index('big')) # 4

    # Useful functions
    str.startswith('The') # True
    str.endswith('goose') # False
    
    # split string based on delimiter (default whitespace)
    str.split() # ['The', 'big', 'bang']
    datestr = '1956-01-31'
    year, month, day = datestr.split('-') # ['1956', '01', '31']
    
    # join combines strings based on a seperator
    ' 👏 '.join([month, day, year]) # '01 👏 31 👏 1956'
    
    # formatting strings automatically calls str() on values
    str = 'Greetings, {}, you are the {}th visitor'.format('Oz', 9)
    print(str)

    num = 91234000.123
    str = (
        '2 decimals: {:.2}, '
        '2 decimal float: {:.2f}'
        '3 decimals as percent: {:.3%} '
        'comma seperated: {:,}'
        ).format(num, num, num, num)
    print(str)

    # select argument from format parameters
    str = '{0}... Welcome {1}, {0}'.format('Oz', 'home')
    print(str)

## Dictionaries ###########################################################
prices = {'coach':20, 'business':28, 'luxury':39.99}
prices['luxury'] # 39.99
prices['coach'] = 14.99 # sets the value
prices['economy'] = 10 # adds a new key/value pair

# Dictionary comprehensions
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_initials = {planet: planet[0] for planet in planets}
print(planet_initials)

# Can be checked
'luxury' in prices # True

# Can be looped over
for key in prices:
    print('{}: ${}'.format(key, prices[key]))

# Keys and values can be iterated over simultaneously
# by retireving the dictionary items (key/val pairs)
print('\nIterating keys and values simultaneously')
for key, val in prices.items():
    print('{}: ${}'.format(key, val))

# Can retrieve all keys or values
prices.keys() # ['coach', 'business', 'luxury', 'economy']
prices.values()
