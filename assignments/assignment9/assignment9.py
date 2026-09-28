

import doctest

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR,
#  month is a acceptable month, 1-12 to represent January-December
#  and day is a acceptable day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2

ShowInfo = tuple[Date, list[str], str, str]
SHOW_DATE = 0
ACTOR_LIST = 1
SHOW_CATEGORY = 2
SHOW_TITLE = 3

# column numbers of data within input csv file
INPUT_SID        = 0
INPUT_TITLE      = 2
INPUT_CAST       = 4
INPUT_DATE       = 6
INPUT_CATEGORIES = 10


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


#helper function used in assignment 8
def create_date(input : str) -> Date:

  '''
  Creates an instance of custom data type Date using the given data and
  returns it

  >>> create_date('10-Jan-18')
  (2018, 1, 10)

  >>> create_date('22-Feb-00')
  (2000, 2, 22)
  '''

  # Removes '-' from the input date and makes it into a list
  input = input.split('-')

  # Converts day value to int
  day = int(input[0])

  # Converts year value to int and adds 2000 to normalise it
  year = 2000 + int(input[2])

  # Uses helper function find_month() to convert month in string to number value
  month = find_month(input[1])

  # Creates instance of custom data type Date with previously set variable
  date = Date([year, month, day])

  # Returns the newly created Date variable
  return date


def read_file(filename: str) -> (dict[str, Date],
                                 dict[str, list[str]],
                                 dict[str, list[str]],
                                 dict[str, str]):
    """
    Populates and returns a tuple with the following 4 dictionaries
    with data from acceptable filename.

    4 dictionaries returned as a tuple:
    - dict[show id: date added to Netflix]
    - dict[show id: list of unique actor names]
    - dict[category: list of unique show ids]
    - dict[show id: show title]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added
    to the dictionary dict[show id: list of unique actor names]

    The list of actors for each key in
      dict[show id: list of unique actor names]
      should be in the order they appear on the line in the input file.
      If the line has duplicated actor names, the unique actor name
      is added once for the first time it occurs in the line.

    Precondition: file is csv with data in expected columns
        and contains a header row with column titles
        Show ids within the file are unique.

    >>> read_file('/content/drive/MyDrive/Assignment 9/0lines_data.csv')
    ({}, {}, {}, {})

    >>> read_file('/content/drive/MyDrive/Assignment 9/11lines_data.csv')  # doctest: +NORMALIZE_WHITESPACE
    ({'81217749': (2019, 11, 15),
      '70303496': (2018, 9, 6),
      '70142798': (2018, 9, 5),
      '80999063': (2018, 10, 5),
      '80190843': (2018, 9, 7),
      '80119349': (2017, 9, 29),
      '70062814': (2018, 9, 5),
      '80182115': (2017, 9, 29),
      '80187722': (2018, 10, 12),
      '70213237': (2018, 10, 2),
      '70121522': (2019, 8, 1)},
     {'81217749': ['Naseeruddin Shah'],
      '70303496': ['Aamir Khan',
                   'Anuskha Sharma',
                   'Sanjay Dutt',
                   'Saurabh Shukla',
                   'Parikshat Sahni',
                   'Sushant Singh Rajput',
                   'Boman Irani',
                   'Rukhsar'],
      '70142798': ['Jirayu La-ongmanee',
                   'Charlie Trairat',
                   'Worrawech Danuwong',
                   'Marsha Wattanapanich',
                   'Nicole Theriault',
                   'Chumphorn Thepphithak',
                   'Gacha Plienwithi',
                   'Suteerush Channukool',
                   'Peeratchai Roompol',
                   'Nattapong Chartpong'],
      '80999063': ['Elyse Maloway',
                   'Vincent Tong',
                   'Erin Matthews',
                   'Andrea Libman',
                   'Alessandro Juliani',
                   'Nicole Anthony',
                   'Diana Kaarina',
                   'Ian James Corlett',
                   'Britt McKillip',
                   'Kathleen Barr'],
      '70062814': ['Ananda Everingham',
                   'Natthaweeranuch Thongmee',
                   'Achita Sikamana',
                   'Unnop Chanpaibool',
                   'Titikarn Tongprasearth',
                   'Sivagorn Muttamara',
                   'Chachchaya Chalemphol',
                   'Kachormsak Naruepatr'],
      '80187722': ['Frank Grillo'],
      '70213237': ['Graham Chapman',
                   'Eric Idle',
                   'John Cleese',
                   'Michael Palin',
                   'Terry Gilliam',
                   'Terry Jones'],
      '70121522': ['Aamir Khan',
                   'Kareena Kapoor',
                   'Madhavan',
                   'Sharman Joshi',
                   'Omi Vaidya',
                   'Boman Irani',
                   'Mona Singh',
                   'Javed Jaffrey']},
     {'Documentaries': ['81217749', '80119349', '80182115'],
      'International Movies': ['81217749',
                               '70303496',
                               '70142798',
                               '80119349',
                               '70062814',
                               '70121522'],
      'Comedies': ['70303496', '70121522'],
      'Dramas': ['70303496', '70121522'],
      'Horror Movies': ['70142798', '70062814'],
      'Children & Family Movies': ['80999063'],
      'Docuseries': ['80190843', '80187722', '70213237'],
      'British TV Shows': ['70213237']},
     {'81217749': 'SunGanges',
      '70303496': 'PK',
      '70142798': 'Phobia 2',
      '80999063': 'Super Monsters Save Halloween',
      '80190843': 'First and Last',
      '80119349': 'Out of Thin Air',
      '70062814': 'Shutter',
      '80182115': 'Long Shot',
      '80187722': 'FIGHTWORLD',
      '70213237': "Monty Python's Almost the Truth",
      '70121522': '3 Idiots'})
    """

    date_dict = {}
    cast_dict = {}
    category_dict = {}
    title_dict = {}


    file = open(filename, "r")
    file.readline() # To read header file and skip it
    lines = file.readlines()

    for line in lines:

      line = line.split(',')

      # Sets values to all the variables from each line
      show_id = line[INPUT_SID]

      date = create_date(line[INPUT_DATE])
      title = line[INPUT_TITLE]
      cast_list = line[INPUT_CAST].split(':')
      category_list = line[INPUT_CATEGORIES].split(':')

      # Creates dictionary entries for date and title dictionaries
      date_dict[show_id] = date
      title_dict[show_id] = title

      # Creates a list to store unique actor names
      unique_cast_list = []

      # For loop to find unique names and store it in unique_cast_list
      for actor in cast_list:
        if actor not in unique_cast_list:
          unique_cast_list.append(actor)

      # Creates dictionary entries for cast dictionaries as long as cast list
      # is not empty
      if unique_cast_list != ['']:
        cast_dict[show_id] = unique_cast_list

      for category in category_list:

        if category in category_dict:
          category_dict[category].append(show_id)
        else:
          category_dict[category] = [show_id]

    return date_dict, cast_dict, category_dict, title_dict
  

#helper function made before in assignment 8
def convert_to_days(date : Date) -> int:

  '''
  Converts the given date into days by multiplying the years and months by
  the number of days in them and adding the days. Not fully accurate, but works
  accurately for the current purpose.

  >>> convert_to_days((2018, 1, 10))
  736215

  >>> convert_to_days((2000, 2, 22))
  729687
  '''

  days = (365 * (date[YEAR] - 1)) + (30 * (date[MONTH] - 1)) + (date[DAY])

  # Returns the amount of days
  return days

def is_before(date : Date, check_date : Date) -> bool:

  '''
  Compares two dates and returns True is the first date is before the second
  date
  '''

  date = convert_to_days(date)
  check_date = convert_to_days(check_date)

  if date < check_date:
    return True
  else:
    return False


def query(filename: str, category: str, date: Date, actors: list[str]
          ) -> list[tuple[str, str]]:
    """
    returns a list of sorted tuples containing (show title, show id) pairs
    of only those shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
    - were added to Netflix before the given date

    Precondition: category and actor names must match case exactly.
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'

    You MUST call read_file and use look ups in the returned dictionaries
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.

    >>> query('/content/drive/MyDrive/Assignment 9/0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []

    >>> query('/content/drive/MyDrive/Assignment 9/11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    [('3 Idiots', '70121522'), ('PK', '70303496')]

    >>> query('/content/drive/MyDrive/Assignment 9/11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    [('3 Idiots', '70121522'), ('PK', '70303496')]

    >>> query('/content/drive/MyDrive/Assignment 9/11lines_data.csv', 'Comedies', (2019, 9, 5), ['Sanjay Dutt'])
    [('PK', '70303496')]

    >>> query('/content/drive/MyDrive/Assignment 9/11lines_data.csv', 'International Movies', (2019, 9, 5), \
    ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('3 Idiots', '70121522'), ('PK', '70303496'), ('Shutter', '70062814')]

    >>> query('/content/drive/MyDrive/Assignment 9/11lines_data.csv', 'International Movies', (2019, 8, 1), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    [('PK', '70303496'), ('Shutter', '70062814')]

    >>> query('/content/drive/MyDrive/Assignment 9/11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either'])
    []

    >>> query('/content/drive/MyDrive/Assignment 9/11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'not found', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]

    >>> query('/content/drive/MyDrive/Assignment 9/11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'Aamir Khan', 'not found either']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]

    >>> query('/content/drive/MyDrive/Assignment 9/11lines_data.csv', 'Comedies', (2019, 9, 5), \
              ['not found', 'not found either', 'Aamir Khan']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('PK', '70303496')]

    >>> query('/content/drive/MyDrive/Assignment 9/large_data.csv', 'Comedies', (2019, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('PK', '70303496')]

    >>> query('/content/drive/MyDrive/Assignment 9/large_data.csv', 'Comedies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'),
     ('PK', '70303496'), ('Zed Plus', '81213884')]

    >>> query('/content/drive/MyDrive/Assignment 9/large_data.csv', 'International Movies', (2020, 9, 5), \
              ['Aamir Khan', 'Mona Singh', 'Achita Sikamana']\
             ) # doctest: +NORMALIZE_WHITESPACE
    [('3 Idiots', '70121522'), ('Andaz Apna Apna', '20258084'),
     ('Dangal', '80166185'), ('Dhobi Ghat (Mumbai Diaries)', '70144331'),
     ('Dil Chahta Hai', '60021525'), ('Dil Dhadakne Do', '80057585'),
     ('Lagaan', '60020906'), ('Madness in the Desert', '80229953'),
     ('PK', '70303496'), ('Raja Hindustani', '17457962'),
     ('Rang De Basanti', '70047320'), ('Secret Superstar', '80245408'),
     ('Shutter', '70062814'), ('Taare Zameen Par', '70087087'),
     ('Talaash', '70262614'), ('Zed Plus', '81213884')]
    """

    (date_dict, cast_dict, category_dict, title_dict) = read_file(filename)

    output_list = []

    acceptable_category = []
    acceptable_category_date = []
    acceptable_everything = []

    if date_dict == {}:
      return []

    if category not in category_dict:
      return []

    acceptable_category = category_dict[category]

    for show_id in acceptable_category:

      if is_before(date_dict[show_id], date) == True:
        acceptable_category_date.append(show_id)

    for show_id in acceptable_category_date:

      if actors == []:
        acceptable_everything = acceptable_category_date

      for actor in actors:

        if show_id not in cast_dict:
          continue

        elif actor in cast_dict[show_id] and show_id not in acceptable_everything:
          acceptable_everything.append(show_id)

    for show_id in acceptable_everything:

      show_title = title_dict[show_id]

      show = tuple([show_title, show_id])
      output_list.append(show)

    output_list.sort()

    return output_list

