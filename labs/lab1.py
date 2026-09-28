def print_my_info():
    '''
    This function prints out the personal info of the user: the name, age favourite number and the result of the division of the user's favourite number and their age
    
    >>> print_my_info()
        My name is Sahil Sanghvi
        My favourite number is 5
        I am 18 years old
        Here is some math: 5/18 is  0.2777777777777778
    
    
    '''
    user_name = 'Sahil Sanghvi'
    user_age = 18
    user_favourite_number = 5
    result = user_favourite_number/user_age
    
    print(f'My name is {user_name}')
    print(f'My favourite number is {user_favourite_number}')
    print(f'I am {user_age} years old')
    print(f'Here is some math: {user_favourite_number}/{user_age} is ',(result))
    
def print_sum():
    
    '''
    The following function prints the sum of two numbers: 23.2 + 82.4
    
    >>> print_sum()
        105.60000000000001
        
    '''
    
    num1 = 23.2
    num2 = 82.4
    total = num1 + num2
    
    print(total) 