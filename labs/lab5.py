import doctest

CHILD_CHECK = 18
ADULT_CHECK = 64


def print_name_age_v1() -> None: 
    
    '''
    Version 1 of print_name_age: This function takes name and age as input and then prints out a response with the name and the category of the age
    '''
    
    name_prompt = 'Enter your Name: '
    age_prompt = 'Enter your Age: '
    
    
    name = input(name_prompt)
    age = input(age_prompt)
    category = ''
    
    if int(age) < CHILD_CHECK:
        
        category = 'child'
        
    elif int(age) >= CHILD_CHECK and int(age) <= ADULT_CHECK:
        category = 'adult'
        
    else: 
        category = 'senior'

    print('hello',name,category)            
               
def print_name_age_v2() -> None: 

    '''
    Version 2 of print_name_age: This function takes name and age as input and then prints out a response with the name and the category of the age. This function also checks if the entered age is a digit or not
    '''    
    
    name_prompt = 'Enter your Name: '
    age_prompt = 'Enter your Age: '
    
    
    name = input(name_prompt)
    age = input(age_prompt)
    category = ''
    
    if not age.isdigit():
        category = 'you are lying about your age'
        
        
    elif int(age) < CHILD_CHECK:
            
        category = 'child'
            
    elif int(age) >= CHILD_CHECK and int(age) <= ADULT_CHECK:
        category = 'adult'
            
    else: 
        category = 'senior'
            
    print('hello',name,category)            

    
def get_num(minimum : int, prompt : str) -> int:
    '''
    This function makes sure the user enters a valid output and returns the integer
    '''
    
    while True:
        
        input_num = input(prompt)
        
        if input_num.isdigit() and int(input_num) >= minimum :
            return int(input_num)        
        
def print_name_age_v3() -> None:
    
    '''
    Version 3 of print_name_age: This function takes name and age as input and then prints out a response with the name and the category of the age. This function uses get_num to make sure  the user has entered a digit
    '''
    
    name_prompt = 'Enter your Name: '
    age_prompt = 'Enter your age: '
    
    name = input(name_prompt)
    age = get_num(0,age_prompt)
    
    category = ''
    
    if age < CHILD_CHECK:
        
        category = 'child'
        
    elif age >= CHILD_CHECK and age <= ADULT_CHECK:
        category = 'adult'
        
    else: 
        category = 'senior'

    print('hello',name,category)    