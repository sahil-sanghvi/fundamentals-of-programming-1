'''
Q0. The following code attempts to print the total price
of a group of items I would like to buy followed by
the amount of money I will have left in my wallet.
My wallet started with 200 dollars.
There are a few things wrong with this program.
What do you think is wrong and how would you fix it?
'''


print('total of item prices:', 3+4+6+14)
print('wallet balance:', 200 - 3+4+6+14)

You can either add two brackets around the 3+4+6+14 to first add those item prices
or just assign the values to variables and perform the operation later

Answer: 
    
    
    print('total of item prices:', 3+4+6+14)
    print('wallet balance:', 200 - (3+4+6+14))
    
    OR
    
    wallet = 200
    item = 3+4+6+14
    wallet -= item
    
    
    print('total of item prices:', item)
    print('wallet balance:', wallet)    




'''
Q1a. Recall from your math classes that the equation for
the lengths of the sides in a right triangle is:
  a^2 + b^2 = c^2
- using the ^ to indicate "raise to the power of" in the description
- how is "raise to the power of" represented in Python?

Write the code that will print the length of side c of
a right triangle with side a length as 3 and side length b as 4.
'''

a = 3
b = 4

c = (a**2) + (b**2)
c = c**0.5

print('hypotenus length: ', c)

OR

import math

a = 3
b = 4

#c = (a**2) + (b**2)

c = math.sqrt(a**2+b**2)

print('hypotenus length: ', c)


'''
Q1b. Update the program you just wrote so
it is contained within a function.
Test the function by calling it from the shell.
'''
import math

def hypo():

    a = 3
    b = 4

    #c = (a**2) + (b**2)

    c = math.sqrt(a**2+b**2)

    print('hypotenus length: ', c)




'''
Q1c. complete the function below so it prints the lengths
of all sides of the right triangle.
Try to avoid re-writing code you have already written!

Test the function by calling it from the shell.
Your output should look something like this...

Dimensions of this right triangle:
the short sides are length: 3 and 4
the hypotenuse is length:  5.0
'''


import math

def hypo():

    a = 3
    b = 4

    #c = (a**2) + (b**2)

    c = math.sqrt(a**2+b**2)

    print('hypotenus length: ', c)
    
def print_right_triangle_dimensions():
    a = 3
    b = 4
    print('Dimensions of this right triangle: \n')
    print('The short sides are length: ', a , ' and ' , b)
    hypo()
    
print_right_triangle_dimensions()




'''
Q2. What does the following code print when uncommented?
Rewrite this code so that it is contained in a function
and both the code and the output makes it more clear
what the program is doing.
Test your function by calling it from the shell
'''
# print(3.14 * 3.4 ** 2, ',', 2 * 3.14 * 3.4)


'''
Q3. Design a function that prints the area of
a 5.7 acre plot of land in square metres
Assume that 1 acre is 4046.85642 square metres
'''

SQR_METERS_FOR_ACRES = 4046.85642

def acres_to_sqr_meters(acres: float):
    '''
    this function converts inputted acres to sq metres
    
    >>> acres_to_sqr_meters(5.7)
    
    Area is: 23067.081594 sq meters

    '''
    
    sqr_metres = acres * SQR_METERS_FOR_ACRES
    
    print('Area is: ' + sqr_metres,'m^2')