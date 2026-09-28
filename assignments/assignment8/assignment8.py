import doctest

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR,
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2

# represents a Netflix show as (show type, title, directors, cast, date added)
#  where none of the strings are empty strings
NetflixShow = tuple[str, str, list[str], list[str], Date]
TYPE      = 0
TITLE     = 1
DIRECTORS = 2
CAST      = 3
DATE      = 4

# column numbers of data within input csv file
INPUT_TYPE      = 1
INPUT_TITLE     = 2
INPUT_DIRECTORS = 3
INPUT_CAST      = 4
INPUT_DATE      = 6



#custom data type to compare actors
ActorDate = tuple[str,int]
ACTOR = 0
ACTOR_NUM = 1

def find_month(month_str : str) -> int:

  '''
  Converts a three character string version of months to their numerical
  counterparts
  '''

  month_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  month_letter = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

  for i in range(12):
    if month_str == month_letter[i]:
      month = month_no[i]

  return month

def create_date(input_date : str) -> Date:

  '''
  Creates an instance of custom data type Date using the given data and
  returns it

  >>> create_date('10-Jan-18')
  (2018, 1, 10)

  >>> create_date('22-Feb-00')
  (2000, 2, 22)
  '''

  input_date = input_date.split('-')

  day = int(input_date[0])

  year = 2000 + int(input_date[2])

  month = find_month(input_date[1])

  date = Date([year, month, day])

  return date


def splitter(input_line: str) -> list[str]:
  '''
  helper function to help split the strings into a list of strings
  '''
  if len(input_line) == 0:
    
    return []
  
  current = input_line.split(':')
  input_line = current

  return input_line

def read_file(filename: str) -> list[NetflixShow]:
    """ Reads file at filename into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns

    >>> read_file('0lines_data.csv')
    []
    
    >>> read_file('9lines_data.csv')
    [('Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], (2019, 11, 15)), \
('Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], (2018, 9, 6)), \
('Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], (2018, 9, 5)), \
('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), \
('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29)), \
('Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], (2018, 9, 5)), \
('Movie', 'Long Shot', ['Jacob LaMendola'], [], (2017, 9, 29)), ('TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], (2018, 10, 12))]
    """
    # TODO: complete this method according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    
    output_list = []
    
    file = open(filename,'r')
    lines = file.readlines()
    
    for x in range(1,len(lines)):
        
        current_line = lines[x].split(',')
      
        type_movie = current_line[INPUT_TYPE]
        title = current_line[INPUT_TITLE]
        date = create_date(current_line[INPUT_DATE])
        
        directors = splitter(current_line[INPUT_DIRECTORS])
        
        cast = splitter(current_line[INPUT_CAST])
        
        netflix = NetflixShow([type_movie,title,directors,cast,date])
        output_list.append(netflix)    
        
    
                    
    
    file.close()

    return output_list

def convert_to_days(netflix : Date) -> int:

    '''
    Converts the dates to number of days to compare efficiently
  
    >>> convert_to_days((2018, 1, 10))
    736215
  
    >>> convert_to_days((2000, 2, 22))
    729687
    '''
  
    days = (365 * (netflix[YEAR] - 1)) + (30 * (netflix[MONTH] - 1)) + (netflix[DAY])
  
    return days

def get_oldest_titles(show_data: list[NetflixShow]) -> list[str]:
    """ Returns a list of the titles of NetflixShows in show_data
    with the oldest added date

    >>> shows_unique_dates = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett',\
    'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> shows_duplicate_oldest_date = [\
    ('Movie', 'Super Monsters Save Halloween', [],\
    ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman',\
    'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina',\
    'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2017, 9, 29)),\
    ('TV Show', 'First and Last', [], [], (2018, 9, 7)),\
    ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> get_oldest_titles([])
    []
    >>> get_oldest_titles(shows_unique_dates)
    ['Out of Thin Air']
    >>> get_oldest_titles(shows_duplicate_oldest_date)
    ['Super Monsters Save Halloween', 'Out of Thin Air']
    """
    # TODO: complete this function according to the documentation
    
    output_list = []    
    
    if len(show_data) == 0:
        
        return output_list
    
    
    min_date = show_data[0][DATE]
    
    for x in range(len(show_data)):
        
        date = show_data[x][DATE]
  
        if convert_to_days(min_date) > convert_to_days(date):
            
            min_date = date
    
    for x in range(len(show_data)):
        
        
        date = show_data[x][DATE]
        
        if min_date == date:
            output_list.append(show_data[x][TITLE])
    
                    
    return output_list    




def actor_num_shows(actors: list[str]) -> list[ActorDate]:
    '''
    Returns a custom data type with Actor name along with the number of times they have been casted
    '''
    
    output_list = []
    temp_list = []
    for x in actors:
        
        if x not in temp_list:
            
            actor = x
            count = 1
            temp = ActorDate([actor,count])
            output_list.append(temp)
            temp_list.append(x)
            
        else:
            counter = 0
            
            for y in output_list:
                
                if x == y[0]:
                    actor = x
                    count = y[1] + 1
                    output_list[counter] = ActorDate([actor,count])
                counter += 1
                    
                    
    return output_list
                    
                    
def get_actors_in_most_shows(shows: list[NetflixShow]) -> list[str]:
    """ Returns a sorted list of actors that are in the casts of the most shows

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]

    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]

    >>> get_actors_in_most_shows([])
    []

    >>> get_actors_in_most_shows(l_unique_casts) # doctest: +NORMALIZE_WHITESPACE
    ['Emma Stone', 'Hugh Bonneville', 'Lily Travers', 'Michael Cera', \
    'Om Puri', 'Paresh Rawal']

    >>> get_actors_in_most_shows(one_actor_in_multiple_casts)
    ['Jonah Hill']

    >>> get_actors_in_most_shows(actors_in_multiple_casts)
    ['Jonah Hill', 'Om Puri']
    """
    # TODO: complete this function according to the documentation
    
    output_list = []
    Actor_list = []
    
    if len(shows) == 0:
        return output_list
    
   
    for y in range(len(shows)):
            
        for x in range(len(shows[y][3])):
        
            Actor_list.append(shows[y][3][x])
            
            
    Actor_list = actor_num_shows(Actor_list)
    
    max_cast = 0
    
    for x in range(len(Actor_list)):
        
        if max_cast < Actor_list[x][ACTOR_NUM]:
            max_cast = Actor_list[x][ACTOR_NUM]
            
    for x in range(len(Actor_list)):
        
        if Actor_list[x][ACTOR_NUM] == max_cast:
            
            output_list.append(Actor_list[x][ACTOR])
            
    
    output_list.sort()
    return output_list
   

def get_shows_with_search_terms(show_data: list[NetflixShow], terms: list[str]) -> list[NetflixShow]:
    """ returns a list of only those NetflixShow elements in show_data
    that contain any of the given terms in the title.
    If terms is empty, all elements in show_data will be included in the returned list.
    Matching of terms ignores case ('roAD' is found in 'Road to Sangam') and
    matches on substrings ('Sang' is found in 'Road to Sangam')

    Precondition: the strings in terms are not empty strings

    >>> movies = [\
    ('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
     ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor',  \
      'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', \
      'Anupam Kher', 'Madhavan'],  \
     (2018, 8, 2)),\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],  \
     ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',  \
      'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',  \
      'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'],  \
     (2017, 12, 12)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]

    >>> terms1 = ['House']
    >>> terms1_wrong_case = ['hoUSe']

    >>> terms_subword = ['Sang']

    >>> terms2 = ['House', 'Road', 'Basanti']
    >>> terms2_wrong_case = ['house', 'ROAD', 'bAsanti']

    >>> get_shows_with_search_terms([], [])
    []

    >>> get_shows_with_search_terms(movies, []) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor',  \
       'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', \
       'Anupam Kher', 'Madhavan'],  \
      (2018, 8, 2)),\
     ('Movie', "Viceroy's House", ['Gurinder Chadha'],  \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',  \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',  \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'],  \
      (2017, 12, 12)),\
     ('Movie', 'Road to Sangam', ['Amit Rai'], \
       ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
        'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
       (2019, 12, 31))]
    >>> get_shows_with_search_terms([], terms1)
    []

    >>> get_shows_with_search_terms(movies, terms1) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], 
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms1_wrong_case) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms_subword) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', \
       'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', \
       'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], 
      (2018, 8, 2)), \
     ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
        'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
        'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
       (2017, 12, 12)), \
      ('Movie', 'Road to Sangam', ['Amit Rai'], \
       ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
        'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
       (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2_wrong_case) # doctest: +NORMALIZE_WHITESPACE
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], \
      ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', \
       'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', \
       'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], \
      (2018, 8, 2)), \
     ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
      ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
       'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
       'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
      (2017, 12, 12)), \
     ('Movie', 'Road to Sangam', ['Amit Rai'], \
      ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
       'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
      (2019, 12, 31))]
    """
    if len(terms) == 0:
      return show_data
    
    
    matching = []
    lower_terms = []
    
    for term in terms:
        lower_terms.append(term.lower())

    for show in show_data:
        title = show[TITLE].lower()  
        flag = False
        for term in lower_terms:
            if term in title:
                flag = True
                
        if flag == True:
            matching.append(show)

    return matching


def query(show_data: list[NetflixShow]) -> list[str]:
    """
    Returns a sorted list of only the show titles from show_data
    that are acted in by the 'most popular' actors
    where the 'most popular' is defined as the actors in the most shows.

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]
    
    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]
    
    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]
    
    >>> query([])
    []
    
    >>> query(l_unique_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    
    >>> query(one_actor_in_multiple_casts)
    ['Maniac', 'Superbad']

    >>> query(actors_in_multiple_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    """
    
    most_popular = get_actors_in_most_shows(show_data)
    flag = False
    output_list = []
   
    if len(most_popular) == 0:
        return most_popular
    
    for x in show_data:
        
        flag = False
        
        for y in most_popular:
            
            if y in x[CAST]:
                flag = True
                
            
        if flag:
            output_list.append(x[TITLE])
    
    
    output_list.sort()
    return output_list q