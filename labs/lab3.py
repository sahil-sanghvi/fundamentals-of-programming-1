import doctest


GST = 0.05
PST = 0.10

def get_longer(str1: str, str2: str) -> str:
   
    '''
    This function takes two arguments which are strings and compares their length. It returns the string with the higher length and returns the first argument if the length is equal.
    
    >>> get_longer('sahil','holi')
    'sahil'
    
    >>> get_longer('sahil','holiday')
    'holiday'
    
    >>> get_longer('sahil','proof')
    'sahil'
    '''
    #if statement to check if str1 is bigger or equal in length then str2
    if len(str1) >= len(str2):
        return(str1)
            
    # returning str2 by default 
    return(str2)
    
    
def get_tax(food_amount: float, alcohol_amount: float) -> float:
    
    '''
    This function takes two float arguments in which first one is the amount for food and second is amount for alcohol and returns the total tax the restaurant is owed
    
    1) GST is 5% and PST is 10%
    2)Restaurants are required to charge only GST on food sales.
    3)Restaurants are required to charge GST and PST on alcohol sales.
    
    >>> get_tax(100,80)
    17.0
    
    >>> get_tax(89,70)
    14.95
    
    >>> get_tax(45,16)
    4.65
    
    >>> get_tax(0,0)
    0.0
    
    >>> get_tax(80,0)
    4.0
    
    >>> get_tax(0,70)
    10.5
    

    '''
    
    #calculating the tax for food
    tax_food = food_amount * GST
    
    #calculating the tax for alcohol
    tax_alcohol = (alcohol_amount * GST) + (alcohol_amount * PST)
    
    #calculating total tax for food and alcohol
    tax_total = tax_food + tax_alcohol
    
    return tax_total

def get_bill_share(food_amount: float, alcohol_amount: float, num_people: int) -> float:
    '''
    This function takes three arguments which are amount spent on food, amount spent on alcohol and number of people dividing the bill and returns the amount each person has to pay (including taxes) 
    
    >>> get_bill_share(100,80,5)
    39.4
    
    >>> get_bill_share(89,70,8)
    21.74375
    
    >>> get_bill_share(45,17,2)
    33.4
    
    >>> get_bill_share(80,60,1)
    153.0
    '''
    
    #calculating total bill using the get_tax function
    total_bill = food_amount + alcohol_amount + get_tax(food_amount,alcohol_amount)
    
    #calculating the per person bill
    per_person_bill = total_bill/num_people
    
    return per_person_bill