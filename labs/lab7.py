import doctest


departure = str
arrival = str
duration = float
Flight_Information = tuple[departure,arrival,duration]


def swap(input_list: list, pos1: int, pos2: int) -> None:
    
    '''
    This function takes a list and two additional position arguments and swaps the two elements in the list at those positions
    
    '''
    if len(input_list) == 0:
        input_list = input_list
    
    else: 
        bucket = input_list[pos1]
        input_list[pos1] = input_list[pos2]
        input_list[pos2] = bucket
    
    
def index_of_smallest(input_list:list) -> int:
    
    '''
    This function returns the index of the smallest element. If two elements are the same, it returns the index of the first occurence of the element. If the list is empty, the function will return -1
    
    >>> index_of_smallest([12, 6, 2, 22, -14, 10, -2])
    4
    
    >>> index_of_smallest(['a', 'b', 'd', 'c', 'A'])
    4
    
    >>> index_of_smallest(['a', 'b', 'd', 'c', 'a'])
    0
    
    >>> index_of_smallest([])
    -1
    
    '''
    
    
    if len(input_list) == 0:
        return -1
    
    smallest_num = input_list[0]
    smallest_index = 0
    
    for i in range(1,(len(input_list))):
        
        if input_list[i] < smallest_num:
            
            smallest_num = input_list[i]
            smallest_index = i
            
        
            
    return smallest_index

def total_duration(flight_info: list[Flight_Information]) -> float:
    
    '''
    This function takes a list of Flight Information tuples and returns the total duration of all the flights combined
    
    >>> total_duration([('Victoria', 'Mexico City', 5.5), ('Vancouver', 'Toronto', 4)])
    9.5
    
    >>> total_duration([])
    0
    
    >>> total_duration([('Victoria', 'Mexico City', 5.5), ('Vancouver', 'Toronto', 4),('India','USA',10.5),('Switzerland','Africa',5.4)])
    25.4
    
    '''
    
    if len(flight_info) == 0:
        return 0
    
    total_time = 0
    for i in flight_info:
        
        total_time += i[2]
        
    return total_time
    
    
def get_destinations_from(flight_info: list[Flight_Information], departure_city : str):
    
    '''
    This function takes a list of flight information tuples and a departure city. It then should return a list of all the unique destinations that are flown to from the given departure city.
    
    >>> get_destinations_from([],'Sahilville')
    []
    
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75), ('Vancouver', 'Toronto', 4), ('Victoria', 'Calgary', 1.5), ('Victoria', 'Vancouver', 0.5)],'Victoria')
    ['Vancouver', 'Calgary']


    '''
    
    if len(flight_info) == 0:
        return []
    
    cities = []
    
    for i in flight_info:
        
        if i[0] == departure_city and i[1] not in cities:
            cities.append(i[1])
            
            
    return cities