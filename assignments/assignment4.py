import doctest

#PART 1

#1
def get_factors(n: int) -> str:
    
    '''
    This function takes an integer argument and returns a string with the factors of that number.
    
    >>> get_factors(12)
    '1,2,3,4,6,12'
    
    >>> get_factors(60)
    '1,2,3,4,5,6,10,12,15,20,30,60'
    
    >>> get_factors(0)
    ''
    
    '''
    
    factors = ''
    
    for x in range(1,n+1):
        
        if n % x == 0:
            
            if x == n:
                factors = factors + str(x) 
            
            else:
                factors = factors + str(x) + ','
                
    return factors

#2
def get_range_of_factors(start: int, end: int) -> str:
    
    '''
    This function takes a starting and ending point and returns a string containing the factors of all numbers within that range in which the end point is not inclusive
    
    >>> get_range_of_factors(10, 13) 
    '1,2,5,10/n1,11/n1,2,3,4,6,12'
    
    >>> get_range_of_factors(10,17)
    '1,2,5,10/n1,11/n1,2,3,4,6,12/n1,13/n1,2,7,14/n1,3,5,15/n1,2,4,8,16'

    >>> get_range_of_factors(0,7)
    '/n1/n1,2/n1,3/n1,2,4/n1,5/n1,2,3,6'

    '''
    
    factor_string = ''
    
    for i in range(start,end):
        factor_string = factor_string + get_factors(i) + '\n'
            
    return factor_string

#3
def sum_fibonacci_sequence(n:int) -> int:
    
    '''
    This function returns the sum of the first n terms of the fibonacci sequence and returns it as an integer
    
    >>> sum_fibonacci_sequence(7)
    20
    
    >>> sum_fibonacci_sequence(11)
    143
    
    >>> sum_fibonacci_sequence(1)
    0
    
    >>> sum_fibonacci_sequence(0)
    0
    '''
    
    # declaring all needed variables and giving them appropiate values
    current_num = 0
    next_num = 1
    third_num = 0
    
    fibonacci = 0
    
    for i in range(n):
        
        fibonacci += current_num
        
        third_num = current_num + next_num        
        current_num = next_num
        next_num = third_num    
        
    return fibonacci

#PART 2

#1

def print_tail(n:int) -> None:
    
    '''
    This function takes n as an argument and prints and rocket's tail with length n
    '''
    
    tail = '//  '
    
    for x in range(0,n):
       
        tail += '/\\  '
        
    tail += '\\\\'
    
    print(tail)
    
def print_booster(n:int) -> None:
    
    '''
    This function prints out a booster using ascii characters 
    
    '''    
   
    width_length = 2 * (n+1)
    
    
    for i in range(0, n+1):
        diff = n-i
        print('|', end = '')
    
        print('.' * (diff), end = '')
        print('/\\' * (i+1), end = '')
        print('.' * (diff), end = '')
    
        print('.' * (diff), end = '')
        print('/\\' * (i+1), end = '')
        print('.' * (diff), end = '')
    
        print('|', end = '')
    
        print()

    for i in range(0, n+1):
        diff = n-i
        print('|', end = '')
    
        print('.' * (i), end = '')
        print('\\/' * (diff+1), end = '')
        print('.' * (i), end = '')
    
        print('.' * (i), end = '')
        print('\\/' * (diff+1), end = '')
        print('.' * (i), end = '')
    
        print('|', end = '')
    
        print()

    print('+' + '=*' * width_length + '+')
    
def print_instrument_unit(n:int) -> None:
    '''
    This function prints out a instrument unit using ascii characters 
    
    '''    
    
    instrument_length_1 = (2*n) + 1
    instrument_length_2 = 2 * (n+1)
  
    print(f'||' + instrument_length_1 * '~#' + '||')
    print(f'||' + instrument_length_1 * '~#' + '||')
    print(f'+' + instrument_length_2 * '=*' + '+')   
    
def print_lem_adapter(n : int) -> None:
    '''
    This function prints out a lem adapter using ascii characters 
    
    '''    

    instrument_length_1 = 2 * n
    instrument_length_2 = (n+1) * 2
  
    print(' //' + instrument_length_1 * ' %' + '\\\\')
    print('//' + (instrument_length_1 + 1) * ' %' + '\\\\')
    print('+' + instrument_length_2 * '=*' + '+')
    

def print_space_craft(n : int) -> None:
    
    '''
    This function prints out a space craft using ascii characters 
    
    '''

    for i in range(0, n * 2):
  
        space_no = ((n+1)*2)
  
        print(' ' * (space_no - i), end = '')
        print('/' * i, end = '')
        print('**', end = '')
        print('\\' * i,)
  
    print('  +' + '=*' * 2 * n + '+')

def print_rocket_ship(size : int, booster : int) -> None:
   
    '''
    Prints out a rocket ship using the functions made above according to the size and booster size entered by user
    '''
  
    print_space_craft(size)
    
    print_lem_adapter(size)
    
    print_instrument_unit(size)
    
    for i in range(0, booster):
        print_booster(size)
    
    print_tail(size)