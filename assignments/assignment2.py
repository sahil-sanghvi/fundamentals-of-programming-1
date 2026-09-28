import doctest

def check_funds(balance: float, purchase_amount: float) -> None:
    
    '''
    This function takes the balance and purchase amount of the item as function arguments and checks the following cases:
    1) If user has a negative balance
    2) If user is short some amount of money
    3) Prints the balance of the remaining money in the account
    
    >>> check_funds(100,69)
    you will have $ 31.00 left after this purchase
    
    >>> check_funds(-100,80)
    you have a negative balance
    
    >>> check_funds(80,100)
    you are short $ 20.00
    '''
    
    # Checks if balance is negative
    if balance < 0:
        
        print('you have a negative balance')
    
    # Calculates difference and prints it out if difference is positive
    elif balance >= purchase_amount:
        
        difference = balance - purchase_amount
        print(f'you will have $ {difference:.2f} left after this purchase')

    # Calculates amount needed if difference is negative
    elif balance < purchase_amount:
        
        difference = purchase_amount - balance
        print(f'you are short $ {difference:.2f}')
    
def print_biggest(a : float, b : float,c : float) -> None:
    
    '''
    This function takes three numbers which are float as fucnction arguments and prints the highest number out of the three numbers
    
    >>> print_biggest(5,6.5,8)
    8
    
    >>> print_biggest(3.2,10,8)
    10
    
    >>> print_biggest(11,8,9)
    11
    '''
    
    # checks if a is the largest number of the three numbers and prints a
    if a >= b and a >= c :
        print(a)
        
    # checks if b is the largest number of the three numbers and prints b
    elif b >= a and b >= c:
        print(b)
        
    # prints third number because the rest of the numbers are smaller
    else:
        print(c)
        
MILE_TO_INCH = 63360
YARD_TO_INCH = 36
FEET_TO_INCH = 12

def convert_inches(inches:float) -> None:
    '''
    This function takes argument which are total inches and then prints out the inches in equivalent distance broken down into miles, yards, feet and inches
    
    >>> convert_inches(63409)
    1 mi, 1 yd, 1 ft, 1 in

    >>> convert_inches(2)
    0 mi, 0 yd, 0 ft, 2 in
    
    >>> convert_inches(0.6)
    0 mi, 0 yd, 0 ft, 0.6 in
    '''
    miles = inches // MILE_TO_INCH # 1 mile = 63360 inches
    inches %= MILE_TO_INCH
    
    yards = inches // YARD_TO_INCH # 1 yard = 36 inches
    inches %= YARD_TO_INCH
    
    feet = inches // FEET_TO_INCH
    inches %= FEET_TO_INCH
    
    # prints out all the values and units
    print(f'{miles:.0f} mi, {yards:.0f} yd, {feet:.0f} ft, {inches} in')
    
def is_multiple_of(n1 : int,n2 : int) -> None:
    
    '''
    This function takes two function arguments n1 and n2 and checks if n1 is a multiple of n2
    
    >>> is_multiple_of(8,2)
    8 is a multiple of 2
    
    >>> is_multiple_of(9,2)
    9 is not a multiple of 2
    
    >>> is_multiple_of(0,0)
    0 is a multiple of 0
    
    >>> is_multiple_of(4,0)
    4 is not a multiple of 0
    
    
    '''
    
    if n1 == 0 and n2 == 0:
        print(f'{n1} is a multiple of {n2}')
    
    elif n1 == 0:
        print(f'{n1} is a multiple of {n2}')
    
    elif n2 == 0:
        print(f'{n1} is not a multiple of {n2}')
        
    elif n1%n2 == 0:
        print(f'{n1} is a multiple of {n2}')
    
    else:
        print(f'{n1} is not a multiple of {n2}')
        
def display_charges(purchase_price:float, tax_rate:float, member: bool, discount_code:str, country: str) -> None: 
    '''
    This function calculates and displays the final bill for an online shopping site.
    
    >>> display_charges(22.0, 8, False, 'FIRST_PURCHASE', 'Mexico')
    price: $ 12.00
    tax: $ 0.96
    shipping: $ 2.20
    total charge: $15.16

    '''
    
    code1 = 'FIRST_PURCHASE'
    code2 = 'FREQUENT_BUYER'
    code3 = 'NO_DISCOUNT'
    
    
    discount = 0
    shipping = 0
    total_charge = 0
    tax = 0
    
    # if statements to check if a valid discount code has been put
    # calculates discount 
    if discount_code == code1:
        discount = 10
        
    elif discount_code == code2 and member == True:
        discount = 2
    
    elif discount_code == code3:
        discount = 0
    
    
    # calculate shipping    
    if member == True or country == 'Canada' or country == 'canada':
        shipping = 0
        
    else: 
        shipping = purchase_price * (10/100)
        
    total_charge = purchase_price - discount    
    
    if total_charge <= 0:
        total_charge = 0
        
    # calculate tax
    tax = (tax_rate/100)* total_charge
    
    total_charge = total_charge+tax+shipping
    
    purchase_price = purchase_price - discount
    if purchase_price <= 0:
        purchase_price = 0
    
    # Prints the bill
    print(f'price: $ {purchase_price:.2f}')
    print(f'tax: $ {tax :.2f}')
    print(f'shipping: $ {shipping :.2f}')
    print(f'total charge: ${total_charge :.2f}')                
        
            
    

    