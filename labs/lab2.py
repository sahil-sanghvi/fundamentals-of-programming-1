import doctest

def print_longer(str1: str, str2: str):
    '''
    This function takes two arguments which are strings and compares their length. It prints the string with the higher length and prints the first argument if the length is equal.
    
    >>> print_longer('sahil','holi')
    sahil
    
    >>> print_longer('sahil','holiday')
    holiday
    
    >>> print_longer('sahil','proof')
    sahil
    '''
    #if statement to check if str1 is bigger in length then str2
    if len(str1) > len(str2):
        print(str1)
        
    #if statement to check if str2 is bigger in length then str1       
    elif len(str1) < len(str2):
        print(str2)
        
    #else statement to print the first argument if non of the if statements are true
    else:
        print(str1)
        
def print_real_roots(a:float,b:float,c:float):
    
    '''
    This function takes three floating point values that represent the values of a,b, and c in a quadratic equation and prints the roots of the function upto 3 decimal points.
    Note: discriminant = b^2 - 4ac
    
    If discriminant is less than 0, the function prints 'NO REAL ROOTS'
    If discriminant is equal to or more than 0, the function prints the roots seperated by a comma
    If a is equal to 0, the function prints 'ERROR' due to a division by zero error
    
    >>> print_real_roots(1,-3,2)
    2.000,1.000
    
    >>> print_real_roots(0,2,-3)
    ERROR
    
    >>> print_real_roots(2,4,3)
    NO REAL ROOTS
    '''
    discriminant = (b**2) - (4*(a*c))
    
    if (a == 0):
        print('ERROR')
        
    elif( discriminant < 0):
        print('NO REAL ROOTS')
        
    else: 
        
        root1 = (-b + discriminant**0.5)/(2*a)
        root2 = (-b - discriminant**0.5)/(2*a)
        
        print(f'{root1:.3f},{root2:.3f}')
        
def print_zodiac_sign(month:str,day:int):
    '''
    This function prints out your zodiac sign. The first argument is the month (STRING FORMAT) and the second argument is the day (INTEGER). 
    You can enter the month in either first letter capatilized format or all lower case characters.
    Ex - April or april
    
    >>> print_zodiac_sign('January',21)
    Aquarius
    
    >>> print_zodiac_sign('february',21)
    Pisces
    
    >>> print_zodiac_sign('March',21)
    Aries
    
    >>> print_zodiac_sign('April',23)
    Taurus
    
    >>> print_zodiac_sign('may',28)
    Gemini
    
    >>> print_zodiac_sign('june',30)
    Cancer
    
    >>> print_zodiac_sign('July',24)
    Leo
    
    >>> print_zodiac_sign('august',25)
    Virgo
    
    >>> print_zodiac_sign('September',25)
    Libra
    
    >>> print_zodiac_sign('October',24)
    Scorpio
    
    >>> print_zodiac_sign('November',25)
    Sagittarius
     
    >>> print_zodiac_sign('January',1)
    Capricorn
    
    >>> print_zodiac_sign('february',1)
    Aquarius
    
    >>> print_zodiac_sign('March',1)
    Pisces
    
    >>> print_zodiac_sign('April',5)
    Aries
    
    >>> print_zodiac_sign('may',1)
    Taurus
    
    >>> print_zodiac_sign('june',3)
    Gemini
    
    >>> print_zodiac_sign('July',2)
    Cancer
    
    >>> print_zodiac_sign('august',2)
    Leo
    
    >>> print_zodiac_sign('September',5)
    Virgo
    
    >>> print_zodiac_sign('October',4)
    Libra
    
    >>> print_zodiac_sign('November',2)
    Scorpio
    
    >>> print_zodiac_sign('December',6)
    Sagittarius
    '''
    
    if ((month == 'January' or month == 'january') and 20 <= day <= 31) or ((month == 'February' or month == 'february') and 1 <= day <= 18):
        print('Aquarius')
    
    elif ((month == 'February' or month == 'february') and 19 <= day <= 29) or (month == 'March' and 1 <= day <= 20):
        print('Pisces')
    
    elif ((month == 'March' or month == 'march') and 21 <= day <= 31) or ((month == 'April' or month == 'april') and 1 <= day <= 19):
        print('Aries')
    
    elif ((month == 'April' or month == 'april') and 20 <= day <= 30) or ((month == 'May' or month == 'may') and 1 <= day <= 20):
        print('Taurus')
    
    elif ((month == 'May' or month == 'may') and 21 <= day <= 31) or ((month == 'June' or month == 'june') and 1 <= day <= 20):
        print('Gemini')
        
    elif ((month == 'June' or month == 'june') and 21 <= day <= 30) or ((month == 'July' or month == 'july') and 1 <= day <= 22):
        print('Cancer')
    
    elif ((month == 'July' or month == 'july') and 23 <= day <= 31) or ((month == 'August' or month == 'august') and 1 <= day <= 22):
        print('Leo')
        
    elif ((month == 'August' or month == 'august') and 23 <= day <= 31) or ((month == 'September' or month == 'september') and 1 <= day <= 22):
        print('Virgo')
        
    elif ((month == 'September' or month == 'september') and 23 <= day <= 30) or ((month == 'October' or month == 'october') and 1 <= day <= 22):
        print('Libra')
    
    elif ((month == 'October' or month == 'october') and 23 <= day <= 31) or ((month == 'November' or month == 'november') and 1 <= day <= 21):
        print('Scorpio')
    
    elif ((month == 'November' or month == 'november') and 22 <= day <= 30) or ((month == 'December' or month == 'december') and 1 <= day <= 21):
        print('Sagittarius')
    
    else:
        print('Capricorn')