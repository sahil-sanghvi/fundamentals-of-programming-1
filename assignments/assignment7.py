import doctest


# Creating custom data type

Date = tuple[int, str, int]

YEAR = 0
MONTH = 1
DAY = 2


# Creating new data type
ShowInfo = tuple[str, str, list:[str], list:[str], Date]

SHOWTYPE = 0
TITLE = 1
DIRECTORS = 2
ACTORS = 3
SHOWDATE = 4


# 1
def raise_to_power(base : list[int], powers : list[int]) -> None:

  '''
  Raises all the elements of the first list to the powers of corresponding
  values in the second list.
  '''

 
  powers_len = len(powers)

  for x in range(len(base)):

    if x>=powers_len:
      power = 1

    else:
      power = powers[x]

    base[x] = base[x] ** power


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

def create_date(input : str) -> None:

  '''
  Creates an instance of custom data type Date using the given data and
  returns it

  >>> create_date('10-Jan-18')
  (2018, 1, 10)

  >>> create_date('22-Feb-00')
  (2000, 2, 22)
  '''

  input = input.split('-')

  day = int(input[0])

  year = 2000 + int(input[2])

  month = find_month(input[1])

  date = Date([year, month, day])

  return date


# Function 5
def create_show(name : str, title : str, directors : list[str], actors : list[str], date : str) -> ShowInfo:

  '''
  Creates an instance of custom data type ShowInfo using the given data
  and returns it.

  >>> create_show('Movie', 'Audrey & Daisy', 'Bonni Cohen:Jon Shenk', \
  '', '23-Sep-16') # doctest: +NORMALIZE_WHITESPACE
  ('Movie', 'Audrey & Daisy', ['Bonni Cohen', 'Jon Shenk'], [], (2016, 9, 23))

  >>> create_show('Movie', 'Room on the Broom', 'Max Lang:Jani Lachauer', \
  'Simon Pegg:Gillian Anderson:Rob Brydon:Martin Clunes:Sally Hawkins:David Walliams:Timothy Spall', \
  '1-Jul-19') # doctest: +NORMALIZE_WHITESPACE
  ('Movie', 'Room on the Broom', ['Max Lang', 'Jani Lachauer'], \
  ['Simon Pegg', 'Gillian Anderson', 'Rob Brydon', 'Martin Clunes', \
  'Sally Hawkins', 'David Walliams', 'Timothy Spall'], \
  (2019, 7, 1))

  >>> create_show('Movie', 'Titanic', '', '', '11-Jul-13')
  ('Movie', 'Titanic', [], [], (2013, 7, 11))
  '''

  if actors == '':
    actors = []
  else:
    actors = actors.split(':')

  if directors == '':
    directors = []
  else:
    directors = directors.split(':')

  date = create_date(date)

  show = ShowInfo ([name, title, directors, actors, date])

  return show


# Function 6
def get_titles(shows : list[ShowInfo]) -> list[str]:

  '''
  Returns the list of titles from a given list of shows

  >>> loshows = [\
  ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
  ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
  'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
  'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
  (2017, 12, 12)),\
  ('Movie', 'Superbad', ['Greg Mottola'], \
  ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
  'Joe Lo Truglio', 'Kevin Corrigan'],\
  (2019, 9, 1)),\
  ('TV Show', 'Maniac', [], \
  ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
  'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
  'Jemima Kirke'], \
  (2018, 9, 21)),\
  ('Movie', 'Road to Sangam', ['Amit Rai'], \
  ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
  'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
  (2019, 12, 31))]

  >>> get_titles(loshows)
  ["Viceroy's House", 'Superbad', 'Maniac', 'Road to Sangam']
  '''

  titles_list = []

  for i in range(len(shows)):

    titles_list.append(shows[i][TITLE])

  return titles_list


def is_actor_in_show(show : ShowInfo, actor_name : str) -> bool:

  '''
  Returns a list of shows that the given actor has acted in

  >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
  ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
  'Joe Lo Truglio', 'Kevin Corrigan'], \
  (2019, 9, 1)), \
  'Justin Bieber')
  False

  >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
  ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
  'Joe Lo Truglio', 'Kevin Corrigan'], \
  (2019, 9, 1)), \
  'Michael Cera')
  True

  >>> is_actor_in_show (('Movie', 'Superbad', ['Greg Mottola'],\
  ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse','Bill Hader',\
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann',\
  'Joe Lo Truglio', 'Kevin Corrigan'], \
  (2019, 9, 1)), \
  'MichaEL cerA')
  True
  '''

  actors_list = []

  for i in range(len(show[ACTORS])):
    actors_list.append(show[ACTORS][i].lower())

  if actor_name.lower() in actors_list:
    return True
  else:
    return False


def convert_to_days(date : ShowInfo) -> int:

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

  return days

def count_shows_before_date(show_list : list[ShowInfo], check_date : Date) -> int:

  '''
  Returns the number of shows released before the given date

  >>> loshows = [\
  ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
  ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi',\
  'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith',\
  'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
  (2017, 2, 6)),\
  ('Movie', 'Superbad', ['Greg Mottola'], \
  ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
  'Joe Lo Truglio', 'Kevin Corrigan'],\
  (2019, 9, 1)),\
  ('TV Show', 'Maniac', [], \
  ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
  'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
  'Jemima Kirke'], \
  (2018, 9, 21)),\
  ('Movie', 'Road to Sangam', ['Amit Rai'], \
  ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
  'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
  (2017, 4, 18))]

  >>> count_shows_before_date(loshows, (2015, 1, 1))
  0

  >>> count_shows_before_date(loshows, (2018, 10, 20))
  3
  '''

  check_date_days = convert_to_days(check_date)
  total_dates = 0

  for i in range(len(show_list)):

    current_date_days = convert_to_days(show_list[i][SHOWDATE])

    if current_date_days < check_date_days:
      total_dates += 1

  return total_dates


def get_shows_with_actor(show_list : list[ShowInfo], check_actor : str) -> list[ShowInfo]:

  '''
  Returns the shows which have the given actor starring in them

  >>> loshows = [\
  ('Movie', "Viceroy's House", ['Gurinder Chadha'], \
  ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', \
  'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', \
  'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], \
  (2017, 12, 12)),\
  ('Movie', 'Superbad', ['Greg Mottola'], \
  ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
  'Joe Lo Truglio', 'Kevin Corrigan'], \
  (2019, 9, 1)),\
  ('TV Show', 'Maniac', [], \
  ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
  'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
  'Jemima Kirke'], \
  (2018, 9, 21)),\
  ('Movie', 'Road to Sangam', ['Amit Rai'], \
  ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', \
  'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], \
  (2019, 12, 31))]

  >>> get_shows_with_actor(loshows, 'Jonah Hill')  # doctest: +NORMALIZE_WHITESPACE
  [('Movie', 'Superbad', ['Greg Mottola'], \
  ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
  'Joe Lo Truglio', 'Kevin Corrigan'], \
  (2019, 9, 1)), \
  ('TV Show', 'Maniac', [], \
  ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
  'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
  'Jemima Kirke'], \
  (2018, 9, 21))]

  >>> get_shows_with_actor(loshows, 'jonaH hiLL')  # doctest: +NORMALIZE_WHITESPACE
  [('Movie', 'Superbad', ['Greg Mottola'], \
  ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', \
  'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', \
  'Joe Lo Truglio', 'Kevin Corrigan'], \
  (2019, 9, 1)), \
  ('TV Show', 'Maniac', [], \
  ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', \
  'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', \
  'Jemima Kirke'], \
  (2018, 9, 21))]

  >>> get_shows_with_actor(loshows, 'Justin Bieber')
  []
  '''

  shows_with_actor = []

  for i in range(len(show_list)):

    if is_actor_in_show(show_list[i], check_actor) == True:
      shows_with_actor.append(show_list[i])

  return shows_with_actor
