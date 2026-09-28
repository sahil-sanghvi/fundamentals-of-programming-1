import doctest
from race_time import RaceTime
from race_result import RaceResult

# represents a racer as (name, country)
# where name and country != ''
RacerNameCountry = tuple[str, str]

# columns of values in input file row and positions in RacerNameCountry
NAME = 0
COUNTRY = 1
TIME_MS = 2

MINS_TO_MS = 60000
SEC_TO_MS = 1000

def read_file(filename: str) -> list[RaceResult]:
    """ returns a list of RaceResults populated with data from filename
    Precondition: the file exists, is not empty, has the following
      information on each row separated by commas:
      racer's name, racer's country, race time in milliseconds>=0
      and contains a header row with the column titles.
      The header row is ignored.

    >>> read_file('0lines_data.csv')
    []
    >>> read_file('9lines_data.csv') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Evan Jager', 'United States', RaceTime(450, 0, 8)), \
     RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7)), \
     RaceResult('Saif Saaeed Shaheen', 'Qatar', RaceTime(630, 53, 7)), \
     RaceResult('Wander Moura', 'Brazil', RaceTime(410, 14, 8)), \
     RaceResult('Mahiedine Mekhissi-Benabbad', 'France', RaceTime(90, 0, 8)), \
     RaceResult('Peter Renner', 'New Zealand', RaceTime(50, 14, 8))]
    """
    # TODO: complete this function
    
    file = open(filename,'r')
    lines = file.readlines()

    output_list = []
    output_dict = {}
    
    for line in lines[1:]:
        
        
        current_line = line.split(',')
        name = current_line[NAME].strip()
        country = current_line[COUNTRY].strip()
        time = int(current_line[TIME_MS].strip())
        
        mins = time//MINS_TO_MS
        time = time - (mins*MINS_TO_MS)
        
        sec = time//SEC_TO_MS
        time = time - (sec*SEC_TO_MS)
        
        ms = time
        race_time = RaceTime(ms,sec,mins)
        
        current_player = RaceResult(name,country,race_time)
        
        output_list.append(current_player)
    
    return output_list
        
                                


def find_athlete(loresults: list[RaceResult], name: str) -> int:
    """ returns the position of RaceResult with given athlete name in loresults
    Returns -1 if name not found
    Returns the position of the first if there >1 RaceResult with given name
    Precondition: case sensitive (ie. 'Brad' != 'brad')

    >>> find_athlete([], 'Brimin Kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))],\
        'brimin kipruto')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Brimin Kipruto')
    1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Brimin Kipruto', 'Kenya', RaceTime(640, 53, 7))], \
        'Peter Renner')
    -1
    >>> find_athlete(\
        [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 22, 20)), \
         RaceResult('Usain Bolt', 'Canada', RaceTime(1, 2, 2019))], \
        'Usain Bolt')
    0
    """
    # TODO: complete this function
    
    len_results = len(loresults)
    
    for i in range(len_results):
        
        if loresults[i].get_name() == name:
            return i
        
    return -1

def get_all_from_country(loresults: list[RaceResult], country: str
                         ) -> list[RaceResult]:
    """ returns a list of all results of the given country
    Precondition: case sensitive (ie. 'Canada' != 'canada')

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 12)), \
     RaceResult('Perrier', 'France', RaceTime(1, 23, 18)), \
     RaceResult('Perrieruels', 'Canada', RaceTime(3, 29, 0)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country([], 'Jamaica')
    []

    >>> get_all_from_country(results, 'jamaica')
    []

    >>> get_all_from_country(results, 'Jamaica') # doctest: +NORMALIZE_WHITESPACE
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 4)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 8, 3)), \
     RaceResult('Allen', 'Jamaica', RaceTime(9, 15, 5))]

    >>> get_all_from_country(results, 'Japan')
    []
    """
    # TODO: complete this function
    output_list = []
    
    if loresults == []:
        return output_list

    for result in loresults:
        
        if result.get_country() == country:
            output_list.append(result)

    return output_list

def race_time_to_ms(time: RaceTime) -> int:
    '''
    This function converts an instance of racetime to ms
    
    >>> rt121920a = RaceTime(12, 19, 25)
    >>> race_time_to_ms(rt121920a)
    1519012
    
    >>> rt121920b = RaceTime(12, 19, 28)
    >>> race_time_to_ms(rt121920b)
    1699012
    
    >>> rt121921  = RaceTime(12, 49, 21)
    >>> race_time_to_ms(rt121921)
    1309012
    
    >>> rt121820  = RaceTime(12, 18, 20)
    >>> race_time_to_ms(rt121820)
    1218012
    
    >>> rt111920  = RaceTime(11, 29, 20)
    >>> race_time_to_ms(rt111920)
    1229011
    
    
    
    '''
    
    mins = time.get_mins()
    sec = time.get_sec()
    ms = time.get_ms()
    
    total_time = (mins*MINS_TO_MS) + (sec*SEC_TO_MS) + ms
    
    
    return total_time


def get_fastest_time(loresults: list[RaceResult]) -> RaceTime:
    """ returns the fastest RaceTime of all finish_times of 
    RaceResult instances in loresults
    Precondition: loresults is not empty

    >>> one_result = [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 9))]
    >>> results = \
    [RaceResult('Allen', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 16, 17)), \
     RaceResult('Barnes', 'Canada', RaceTime(3, 43, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 29, 9)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 48, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 17))]

    >>> get_fastest_time(one_result)
    RaceTime(12, 31, 9)
    >>> get_fastest_time(results)
    RaceTime(3, 29, 9)
    """
    # TODO: complete this function
    fastest_time = 1000000
    fastest_instance = RaceTime(100,100,100)
    
    for result in loresults:
        
        time = result.get_finish_time()
        
        if time.is_faster(fastest_instance):
            fastest_time = race_time_to_ms(time)
            fastest_instance = time
    
    return fastest_instance


def get_with_fastest_time(loresults: list[RaceResult]
                          ) -> list[RacerNameCountry]:
    """ returns a list tuples of fastest RaceResults in loresults

    >>> results = \
    [RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 31, 10)), \
     RaceResult('Zhou', 'China', RaceTime(9, 15, 6)), \
     RaceResult('Barnes', 'Canada', RaceTime(1, 23, 9)), \
     RaceResult('Perrier', 'France', RaceTime(3, 10, 7)), \
     RaceResult('Bailey', 'Jamaica', RaceTime(2, 15, 9)), \
     RaceResult('Davis', 'Jamaica', RaceTime(9, 15, 6))]
     
    >>> get_with_fastest_time([])
    []
    >>> get_with_fastest_time(results)
    [('Zhou', 'China'), ('Davis', 'Jamaica')]
    """
    # TODO: complete this function
    output_list = []
    
    if loresults == []:
        return output_list
    
    fastest_time = get_fastest_time(loresults)
    
    for result in loresults:
        
        if result.get_finish_time() == fastest_time:
            
            name = result.get_name()
            country = result.get_country()
            
            racer = RacerNameCountry([name,country])
            
            output_list.append(racer)
            
            
    return output_list