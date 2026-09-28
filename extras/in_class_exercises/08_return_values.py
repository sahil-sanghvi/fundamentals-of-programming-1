import doctest

ADULT = 18
SENIOR = 65
CHILD_RATE = 1.50
ADULT_RATE = 2.50
SENIOR_RATE = 2.00

'''
Q0. Design a function that will take two numbers and
returns the sum of those numbers
'''
def get_sum(a:float,b:float) -> float:
    '''
    This function takes two numbers as an input and returns the sum of the numbers
    
    >>> get_sum(4,-7)
    -3
    
    >>> get_sum(2.2,3.6)
    5.800000000000001
    '''
    
    total = a + b
    
    return total

'''
Q0b. Design a function that will take two numbers and prints the average
of those numbers.
In your function body, call the funtion desiged in Q1a
to practice calling a function from another function.
'''
def get_average(a:float,b:float) -> None:
    '''
    This function takes two numbers and returns the average of those numbers
    
    >>> get_average(4,-7)
    -1.5
    '''
    average = get_sum(a,b)/2
    
    print(average)  

'''
Q0c. If the function you designed in Q0a printed the sum instead of
returning it, would you average function still behave as expected?
'''

'''
Q1. Below is the print_fare function we wrote in a past lecture.
Continuing in this problem domain, design a separate function that takes
the number of children, number of adults and number of seniors
and returns the total fare for those riders.
You function should take into acount a group discount of 10%
for groups of 10 or more.
You can assume the function will not be passed negative values.

NOTICE: print_fare does not return a value, so calling it will not be useful
BUT, there are CONSTANTS defined that might be useful!
'''
def get_total_fare(children: int, adults: int, seniors: int) -> float:
    '''
    returning the dare for given children, adults and seniors
    
    >>> get_total_fare(0,0,0)
    0.0
    >>> get_total_fare(2,1,2)
    9.5
    >>> get_total_fare(2,2,2)
    12.0
    >>> get_total_fare(4,3,4)
    19.35
    
    '''
    fares = children * CHILD_RATE + adults * ADULT_RATE + seniors * SENIOR_RATE
    total_people = children+adults+seniors
    
    if total_people >= 10:
        fares = 0.9 * fares
        
    return fares

def print_fare(age: int) -> None:
    """ determines the bus fare for a rider of the given age and prints it
    Precondition: age > 0
    >>> print_fare(0)
    The fare is: $1.50
    >>> print_fare(ADULT-1)
    The fare is: $1.50
    >>> print_fare(ADULT)
    The fare is: $2.50
    >>> print_fare(ADULT+1)
    The fare is: $2.50
    >>> print_fare(SENIOR-1)
    The fare is: $2.50
    >>> print_fare(SENIOR)
    The fare is: $2.00
    >>> print_fare(SENIOR+1)
    The fare is: $2.00
    """
    fare = 0
    if age < ADULT:
        fare = CHILD_RATE
    elif age >= SENIOR:
        fare = SENIOR_RATE
    else:
        fare = ADULT_RATE

    print(f'The fare is: ${fare:.2f}')


'''
Q2. design a function that takes the amount of money in a bank account and
the number of children, number of adults and number of seniors.
You can assume the function will not be passed negative values for
number of people, but the account balance can be negative.

The function should print the total fare for all of these people and
the balance left in the bank account after the fare is paid.
The function should return the balance left in the bank account
after the fare is paid.
'''

def pay_fare(children: int, adults: int, seniors: int,bank_amount:int) -> float:
    '''
    This function prints the total fare for all of these people and
    the balance left in the bank account after the fare is paid.
    
    >>> pay_fare(2,3,4,100)
    Fare: $ 18.5
    Balance Left: $ 81.5
    81.5
    '''
    bank_amount = bank_amount - get_total_fare(children,adults,seniors)
    print('Fare: $',get_total_fare(children,adults,seniors))
    print('Balance Left: $',bank_amount)
          
    return bank_amount



''' Q3. Recall we designed the following function in a past lecture.
Update this function so it does not print the roman numeral,
but instead returns it.'''


def print_roman_numeral(num: int) -> None:
    """ determines and prints the corresponding roman numeral for the given num
    Precondition: 1 <= num <=10
    >>> print_roman_numeral(1)
    I
    >>> print_roman_numeral(2)
    II
    >>> print_roman_numeral(3)
    III
    >>> print_roman_numeral(4)
    IV
    >>> print_roman_numeral(5)
    V
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
    elif num == 5:
        roman_numeral = 'V'
    elif num == 6:
        roman_numeral = 'VI'
    elif num == 7:
        roman_numeral = 'VII'
    elif num == 8:
        roman_numeral = 'VIII'
    elif num == 9:
        roman_numeral = 'IX'
    else:
        roman_numeral = 'X'

    print(roman_numeral)
