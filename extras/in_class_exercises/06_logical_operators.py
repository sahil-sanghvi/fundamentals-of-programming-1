import doctest

ADULT = 18
SENIOR = 65
CHILD_RATE = 1.50
ADULT_RATE = 2.50
SENIOR_RATE = 2.00

NUM_BUNS_PER_PACK = 8
NUM_DOGS_PER_PACK = 12

MIN_TEMP=5
MAX_TEMP=300
COMBINED_MAX_TEMP=250

MIN_PSI=0
MAX_PSI=150
COMBINED_MAX_PSI=100
'''
Q1. You were asked to design a function that determines the cost of
riding the bus based on the value of the argument age of type int.
If age is less than 18, the cost is $1.50.
If age is 65 or more, the cost is $2.00.
For all other values of age, the cost is $2.50.

A friend of yours submitted the following code but was deducted marks for:
-inappropriate use of branching constructs
-redundant Boolean expressions
-magic numbers
-insufficient test coverage
-missing units in output

Edit the function in light of the feedback from the marker.
'''


def print_fare(age: int):
    """ determines the bus fare for a rider of the given age and prints it
    
    Changes:
    -added elif and else
    -replaced magic numbers with global constants
    -added $ for units

    Precondition: age > 0
    >>> print_fare(15)
    The fare is: $1.50
    
    >>> print_fare(21)
    The fare is: $2.50
    
    >>> print_fare(75)
    The fare is: $2.00
    
    >>> print_fare(65)
    The fare is: $2.00
    """
    if age < ADULT:
        fare = CHILD_RATE
    elif age >= SENIOR:
        fare = SENIOR_RATE
    else:
        fare = ADULT_RATE

    print(f'The fare is: ${fare:.2f}')


'''
Q2. The following function design fails some of the given
example tests but there is more than one problem with it.
Find and fix the problems.
'''


def print_roman_numeral(num: int):
    """ determines and prints the corresponding roman numeral for the given num

    >>> print_roman_numeral(1)
    I
    >>> print_roman_numeral(2)
    II
    >>> print_roman_numeral(3)
    III
    >>> print_roman_numeral(4)
    IV
    >>> print_roman_numeral(6)
    VI
    >>> print_roman_numeral(7)
    VII
    >>> print_roman_numeral(8)
    VIII
    >>> print_roman_numeral(9)
    IX
    >>> print_roman_numeral(10)
    X
    """
    roman_numeral = ''

    if num == 1:
        roman_numeral = 'I'
    elif num == 2:
        roman_numeral = 'II'
    elif num == 3:
        roman_numeral = 'III'
    elif num == 4:
        roman_numeral = 'IV'
    elif num==5:
        roman_numeral = 'V'
    elif num == 6:
        roman_numeral = 'VI'
    elif num == 7:
        roman_numeral = 'VII'
    elif num == 8:
        roman_numeral = 'VIII'
    elif num == 9:
        roman_numeral = 'IX'
    elif num== 10:
        roman_numeral = 'X'
    else:
        roman_numeral="error"

    print(roman_numeral)


'''
Q3. Design a function that takes 2 numbers representing an (x,y) point on a
graph and prints what quadrant it is in.  RECALL:  quadrants are numbered
1 through 4 counter clockwise starting at the upper right quadrant.

The function should print: '(x# , y#)' where x# and y# are the x,y arguments
if x and y are zero it should then print 'at center'
otherwise if x or y are zero it should print which axis it is on:
'on x-axis' or 'on y-axis'
otherwise it should print 'Q#' where # is the quadrant number it is in
'''
def quadrant_sign(x, y):
    '''
    Function that takes 2 numbers representing an (x,y) point on a
    graph and prints what quadrant it is in.
    
    >>> quadrant_sign(0,0)
    (0, 0)
    at center
    
    >>> quadrant_sign(3,0)
    (3, 0)
    on x-axis
    
    >>> quadrant_sign(0,3)
    (0, 3)
    on y-axis
    
    >>> quadrant_sign(3,3)
    (3, 3)
    Q1
    
    >>> quadrant_sign(-1,3)
    (-1, 3)
    Q2
    
    >>> quadrant_sign(-1,-1)
    (-1, -1)
    Q3
    
    >>> quadrant_sign(1,-1)
    (1, -1)
    Q4
    '''
    if x==0 and y==0:
        print(f"({x}, {y})")
        print('at center')
        
    elif x==0 or y==0:
        if x==0:
            print(f"({x}, {y})")
            print('on y-axis')
            
        else:
            print(f"({x}, {y})")
            print('on x-axis')
            
    elif x>0 and y>0:
        print(f"({x}, {y})")
        print('Q1')
        
    elif x<0 and y>0:
        print(f"({x}, {y})")
        print('Q2')
        
    elif x<0 and y<0:
        print(f"({x}, {y})")
        print('Q3')
        
    elif x>0 and y<0:
        print(f"({x}, {y})")
        print('Q4')    

'''
Q4. Design a function that takes two numbers:
one for air temperature (in degrees Celsius) and
one for air pressure(in pounds per square inch, psi) inside a mechanical device
The function should print the message "Error: data not valid",
if the pressure is negative, and then terminates
otherwise it should print a message about the machine's operation
according to the following:
If the temperature is above 300 degrees C or below 5 degrees C, or if the
pressure is above 150psi, the machine is not operating under normal conditions.

If the temperature is above 250 degrees C and the pressure is above 100psi,
the machine is not operating under normal conditions.
Otherwise, the machine is operating under normal conditions.

TIP: the temperature and pressure thresholds are all constant value
that should not change during your program.  How/where should you define them?
'''

def machine_operation(degrees, psi):
    '''
    Expected output:
    >>> machine_operation(260, 120)
    The machine is not operating under normal conditions.
    
    >>> machine_operation(350, 120)
    The machine is not operating under normal conditions.
    
    >>> machine_operation(1, 120)
    The machine is not operating under normal conditions.
    
    >>> machine_operation(15, 170)
    The machine is not operating under normal conditions.
    
    >>> machine_operation(200, 120)
    The machine is operating under normal conditions.
    
    >>> machine_operation(260, -120)
    Error: data not valid
    
    '''
    not_normal_1= degrees>MAX_TEMP or degrees<MIN_TEMP or psi>MAX_PSI
    
    not_normal_2= degrees>COMBINED_MAX_TEMP and psi>COMBINED_MAX_PSI
    
    if psi<MIN_PSI:
        
        print("Error: data not valid")
    
    else:
        
        if not_normal_1 or not_normal_2:
            print("The machine is not operating under normal conditions.")
            
        else:
            print("The machine is operating under normal conditions.")


'''
Q5. Write a function that takes the number of people coming
    to a picnic and prints the nubmer of packages of hot dogs and buns to buy
    assume: each person will eat 2 hot dogs and
    the number of buns in a package is NUM_BUNS_PER_PACK and
    the number of dogs in a package is NUM_DOGS_PER_PACK and
Tip: if you know you need 16 hot dogs and there are 8 buns per pack and
12 dogs per pack, you need to know how many whole bags of each you need,
plus an extra bag if the whole bags are not quite enough.
Think about how the results of the following expressions help:
16 // 8
16 % 8
16 // 12
16 % 12
'''
