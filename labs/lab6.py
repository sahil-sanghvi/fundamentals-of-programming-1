import doctest

def sum_even_values(num:list[int]) -> int:
    
    '''
    This function takes a list filled with integers and returns a sum of the even integers from the list
    
    >>> sum_even_values([])
    0
    
    >>> sum_even_values([1,2,3,4,5,6,7,8,9,10])
    30
    
    >>> sum_even_values([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10])
    -30
    
    >>> sum_even_values([-1,2,-3,-4,-5,6,-7,-8,-9,10])
    6
    
    >>> sum_even_values([3,5,7,9,11])
    0
    
    
    '''
    
    sum_even = 0
    
    for x in num:
        if x % 2 == 0: 
            sum_even += x
            
            
    return sum_even


def count_above(num:list[float], threshold:float) -> int:
    
    '''
    This function takes a threshold and a list of numbers as arguments and returns the total number of elements which are above the threshold
    
    >>> count_above([32,43,54,12,23,3,4,123,32,90],5.5)
    8
    
    >>> count_above([],6.8)
    0
    
    >>> count_above([1,2,3,4,5,6,7,8,9],9)
    0
    
    >>> count_above([1,2,3,4,5,6,7,8,9],11)
    0
    
    >>> count_above([3.2,4.3,5.5,5.6,5.7,12,2.3,3,4,123,32,90],5.5)
    6
    
    '''

    count = 0
    
    for x in num:
        
        if x > threshold:
            count += 1
            
    return count


def add1(num:list[int]) -> list[int]:
    
    '''
    This function takes a list of integers as an argument and returns a new list with every value in the given list with added 1 to it
    
    >>> add1([])
    []
    
    >>> add1([1,2,3,4,5,6,7])
    [2, 3, 4, 5, 6, 7, 8]
    
    >>> add1([1,-2,3,4,-5,-6,7])
    [2, -1, 4, 5, -4, -5, 8]

    '''
    num2 = []
    for x in range(0,len(num)):
        
        num2.append(num[x]+1)
        
    return num2
    
def are_all_even(num:list[int]) -> bool:
    
    '''
    This function checks if a list with integers has all even values.
    
    >>> are_all_even([])
    True
    
    >>> are_all_even([1,2,3,4,5,6,7])
    False
    
    >>> are_all_even([2,4,6,7,8])
    False
    
    >>> are_all_even([2,4,6,10,8])
    True
    
    >>> are_all_even([-2,-4,-8])
    True
    
    
    '''
    
    are_even = True
    count = 0
    
    while count < len(num) and are_even == True:
        
        if num[count]%2 != 0:
            are_even = False
            
        count += 1
        
            
    return are_even