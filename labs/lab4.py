import doctest

def compute_harmonic_series(n: int) -> float:
    '''
    This function takes n as an argument and returns the sum of the harmonic series
    
    For example: 
    if n = 5, this function would return the sum of (1/1) + (1/2) + (1/3) + (1/4) + (1/5) = 2.283333333333333
    
    >>> compute_harmonic_series(5)
    2.283333333333333
    
    >>> compute_harmonic_series(0)
    0
    
    >>> compute_harmonic_series(1)
    1.0
    
    >>> compute_harmonic_series(7)
    2.5928571428571425
 
    '''
    
    harmonic_value = 0
    
    
    # for loop which iterates from 1 to n+1 
    for i in range(1,(n+1),1):
        
        harmonic_value = harmonic_value + (1/i)
        
    return harmonic_value 


def get_fibonacci_sequence(n:int) -> str:
    
    '''
    This function takes n as an argument and prints n terms of the fibonacci series.
    
    >>> get_fibonacci_sequence(5)
    '0,1,1,2,3'
    
    >>> get_fibonacci_sequence(9)
    '0,1,1,2,3,5,8,13,21'
    
    >>> get_fibonacci_sequence(0)
    ''
    >>> get_fibonacci_sequence(1)
    '0'
    
    '''
    # declaring all needed variables and giving them appropiate values
    current_num = 0
    next_num = 1
    third_num = 0
    
    fibonacci = ''
    
    for i in range(n):
        
        # if statement to avoid a comma when the last term is getting added to the string
        if i == n-1:
            fibonacci = fibonacci + str(current_num)
        else:
            fibonacci = fibonacci + str(current_num) + ','
        
        third_num = current_num + next_num        
        current_num = next_num
        next_num = third_num
        
    return fibonacci

def print_pattern(height: int, width: int, combi1: str, combi2: str) -> None:
    
    '''
    This function takes height, width and two strings as arguments and prints them in a box with dimensions of the height and width with every odd line printing combi1 first followed by combi2 and every even line prints combi2 first followed by combi1
    
    >>> print_pattern(4,3, '!@', '$$$')
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    
    >>> print_pattern(5,5,'^_^','0_0')
    ^_^0_0^_^0_0^_^0_0^_^0_0^_^0_0
    0_0^_^0_0^_^0_0^_^0_0^_^0_0^_^
    ^_^0_0^_^0_0^_^0_0^_^0_0^_^0_0
    0_0^_^0_0^_^0_0^_^0_0^_^0_0^_^
    ^_^0_0^_^0_0^_^0_0^_^0_0^_^0_0

    '''
    # creating the combinations to use while printing
    mixedcombi1 = combi1 + combi2
    mixedcombi2 = combi2 + combi1
    
    
    for i in range(height):
        for j in range(width):
            
            if i%2 == 0:
                print(mixedcombi1,end = '')
                
            else: 
                print(mixedcombi2,end = '')
                
        print()
        