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
        
       
        third_num = current_num + next_num        
        current_num = next_num
        next_num = third_num
        
    
    if n == 0:
        fibonacci = fibonacci + str(current_num)
            
    return fibonacci + get_fibonacci_sequence(n-1) 
