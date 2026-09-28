import doctest

#PART 1

#1
def get_biggest(a:int, b:int, c:int) -> int:
    
    '''
    This function takes three numbers which are integers as fucnction arguments and returns the highest number out of the three numbers
    
    >>> get_biggest(5,6,8)
    8
    
    >>> get_biggest(3,10,8)
    10
    
    >>> get_biggest(11,8,9)
    11
    '''
    
    # checks if a is the largest number of the three numbers and prints a
    if a >= b and a >= c :
        return a
        
    # checks if b is the largest number of the three numbers and prints b
    elif b >= a and b >= c:
        return b
        
    # prints third number because the rest of the numbers are smaller
    else:
        return c  

#2    
def get_smallest(a:int, b:int, c:int) -> int:
    
    '''
    This function takes three numbers which are integers as fucnction arguments and returns the highest number out of the three numbers
    
    >>> get_smallest(5,6,8)
    5
    
    >>> get_smallest(3,10,8)
    3
    
    >>> get_smallest(11,8,9)
    8
    '''
    
    # checks if a is the smallest number of the three numbers and prints a
    if a <= b and a <= c :
        return a
        
    # checks if b is the smallest number of the three numbers and prints b
    elif b <= a and b <= c:
        return b
        
    # prints third number because the rest of the numbers are bigger
    else:
        return c    
    
#3
def is_multiple_of(n1 : int,n2 : int) -> bool:
    
    '''
    This function takes two function arguments n1 and n2 and checks if n1 is a multiple of n2
    
    >>> is_multiple_of(8,2)
    True
    
    >>> is_multiple_of(4,0)
    False
    
    >>> is_multiple_of(0,0)
    True
    
    >>> is_multiple_of(9,2)
    False
    '''
    
    # if statement for if n1 and n2 are 0, 0 is a multiple of 0
    if n1 == 0 and n2 == 0:
        return True
    
    # if n1 is 0, then True is returned because 0 is a multiple of every number
    elif n1 == 0:
        return True
    
    # if n2 = 0 and n1 is not 0, then n1 is not a multiple of 0
    elif n2 == 0:
        return False
        
    # if statement to check if n1 is a multiple of n2
    elif n1%n2 == 0:
        return True
    
    # else statement to return False if all if statements return false
    else:
        return False

#4
def is_biggest_multiple_of_smallest(a:int, b:int, c:int) -> bool:
    
    '''
    This function takes three arguments which are integer values. It determines whether the biggest of the three values is a multiple of the smallest of the three values.
    
    >>> is_biggest_multiple_of_smallest(10,5,7)
    True
    
    >>> is_biggest_multiple_of_smallest(10,4,7)
    False
    
    >>> is_biggest_multiple_of_smallest(10,0,7)
    False
    
    '''
    
    # assign variable value of biggest integer out of a,b and c
    biggest_num = get_biggest(a,b,c)
    
    # assign variable value of smallest integer out of a,b and c
    smallest_num = get_smallest(a,b,c)
    
    # boolean variable to store True or False where True is when biggest_num is a multiple of smallest_num
    is_biggest_multiple_of_smallest = is_multiple_of(biggest_num,smallest_num)
    
    if is_biggest_multiple_of_smallest == True:
        return True
    
    else:
        return False
    
# PART 2

#1
def get_discount(discount_code: str, member: bool) -> int:
    
    '''
    This function returns the value of the discount applicable according to the discount code which has been given
    
    1) FIRST_PURCHASE is $ 10 off the purchase price
    2) FREQUENT_BUYER and they are a site member it is $ 2 off the purchase price
    3) NO_DISCOUNT or an invalid discount code is $ 0 off the purchase price
    
    >>> get_discount('FIRST_PURCHASE',False)
    10
    
    >>> get_discount('FIRST_PURCHASE',True)
    10
    
    >>> get_discount('FREQUENT_BUYER',False)
    0
    
    >>> get_discount('FREQUENT_BUYER',True)
    2
    
    >>> get_discount('pls give discount', False)
    0
    '''
    
    code1 = 'FIRST_PURCHASE'
    code2 = 'FREQUENT_BUYER'
    code3 = 'NO_DISCOUNT'
    
    #set default value of discount as 0
    discount = 0
    
    # if statements to check if a valid discount code has been put
    # calculates discount 
    if discount_code == code1:
        discount = 10
        
    elif discount_code == code2 and member == True:
        discount = 2
    
    else :
        discount = 0    
        
    return discount

#2
def get_discounted_price(discount_code: str, purchase_price: int, member: bool) -> float:
    
    '''
    This function returns the discounted purchase price using the get_discount function. 
    
    >>> get_discounted_price('FIRST_PURCHASE', 80, False)
    70

    >>> get_discounted_price('FREQUENT_BUYER', 120, True)
    118

    >>> get_discounted_price('FREQUENT_BUYER', 110, False)
    110

    >>> get_discounted_price('pls give discount', 180, False)
    180

    >>> get_discounted_price('FIRST_PURCHASE', 8, False)
    0
    '''
    
    if purchase_price < 0:
        purchase_price = 0
        
    discount = get_discount(discount_code,member)
    
    purchase_price = purchase_price - discount
    
    if purchase_price < 0:
        purchase_price = 0
        
    return purchase_price

#3


SHIPPING_RATE = 0.10
def get_shipping(member:bool, country: str, purchase_price: int) -> float :
    
    '''
    This function calculates and returns the shipping cost. There is no shipping cost if the country is canada or if the user is a member.
    
    >>> get_shipping(True,'USA',100)
    0
    
    >>> get_shipping(False,'USA',100)
    10.0
    
    >>> get_shipping(False,'Canada',100)
    0
    
    >>> get_shipping(True,'Canada',100)
    0

    '''
    
    # setting shipping default value to be 0
    shipping = 0
    
    if member == True or country == 'Canada' or country == 'canada':
        return shipping
    
    else:
        
        shipping = purchase_price * SHIPPING_RATE
        return shipping
    
#4
def display_charges(purchase_price: float, tax_rate: float, member:bool, discount_code: str, country: str) -> None:
    
    '''
    This function prints the bill using the above three functions and calling them when needed
    
    >>> display_charges(22.0, 8, False, 'FIRST_PURCHASE', 'Mexico')
    price: $ 12.00
    tax: $ 0.96
    shipping: $ 2.20
    total charge: $15.16
    '''
    
    
    shipping = get_shipping(member,country,purchase_price)
    
    purchase_price = get_discounted_price(discount_code,purchase_price,member)
    
    tax = (tax_rate/100) * purchase_price
    
    total_price = purchase_price + shipping + tax
    
    # Prints the bill
    print(f'price: $ {purchase_price:.2f}')
    print(f'tax: $ {tax :.2f}')
    print(f'shipping: $ {shipping :.2f}')
    print(f'total charge: ${total_price :.2f}')    