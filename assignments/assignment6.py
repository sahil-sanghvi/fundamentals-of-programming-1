import doctest

def get_powers(number_list : list[float], exponent : float) -> list[float]:

  '''
  Returns a list where all the components have been raised to the exponent given

  >>> get_powers([0],0)
  [1]

  >>> get_powers([1,2,3,4,5,6,7,8],2)
  [1, 4, 9, 16, 25, 36, 49, 64]

  >>> get_powers([-1,-2,-3,4,0], 1)
  [-1, -2, -3, 4, 0]
  '''

  expo_list = []

  # Loop to iterate through all elements of the input list
  for i in range(len(number_list)):

    expo_list.append(number_list[i] ** exponent)

  return expo_list


def concatenate(original_string : list[str]) -> str:

  '''
  Concatenates all the input strings and returns it with spaces between them

  >>> concatenate(['sahil', 'sanghvi'])
  'sahil sanghvi'

  >>> concatenate(['sahil'])
  'sahil'

  >>> concatenate([])
  ''
  
  >>> concatenate(['sahil','sanghvi','best'])
  'sahil sanghvi best'
  
  
  '''

  concencate_string = ''

  for i in range(len(original_string)):
    concencate_string += original_string[i] + ' '

  return concencate_string[:-1]


def contains_multiple(input_list : list[int], factor : int) -> bool:

  '''
  Finds out whether the given list has any multiples of the given integer

  >>> contains_multiple([1,2,3,4,5],1)
  True

  >>> contains_multiple([2,4,6,8,10],2)
  True

  >>> contains_multiple([1,13,5,7,17],3)
  False

  >>> contains_multiple([15, 28, 24, 11, 7, -72], 4)
  True

  >>> contains_multiple([], 18)
  False
  '''

  ismultiple = False

  for i in range(len(input_list)):

    # if statement for factor when factor is 0
    if factor == 0:
      for j in range(len(input_list)):

        if input_list[j] == 0:
          ismultiple = True
          return ismultiple

      ismultiple = False


    elif input_list[i] % factor == 0:
      ismultiple = True
      return ismultiple

    else:
      ismultiple = False

  return ismultiple


def get_long_enough(input_list : list[str], max_length : int) -> str:

  '''
  Returns the list of strings that are longer than then max length provided

  >>> get_long_enough(['sahil','sam','sanghvi','sanjay','karanveer'],5)
  ['sahil', 'sanghvi', 'sanjay', 'karanveer']

  >>> get_long_enough([],5)
  []

  >>> get_long_enough(['sahil','sahil2','sahil35','sahil100','rishonrajesh'],50)
  []

  >>> get_long_enough(['sahil','sam','sanghvi','sanjay','karanveer'],0)
  ['sahil', 'sam', 'sanghvi', 'sanjay', 'karanveer']
  '''

  long_list = []

  for i in range(len(input_list)):

    # Checks if the current items length is bigger than given length
    if len(input_list[i]) >= max_length:
      long_list.append(input_list[i])

  return long_list


def all_multiples(input_list : list[int], factor : int) -> bool:

  '''
  Finds out whether the given list has numbers which are all multiples of the given factor

  >>> all_multiples([1,2,3,4,5],1)
  True

  >>> all_multiples([2,4,6,8,10],2)
  True

  >>> all_multiples([1,13,5,7,17],3)
  False

  >>> all_multiples([-10, 12, -20, -7, 5, 4, 9, -4, 15, -8, -12, -9, 18, 8], 0)
  False

  >>> all_multiples([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
  True
  '''

  flag = True

  if factor == 0:

    for i in range(len(input_list)):

      if input_list[i] != 0:
        return False

    return True

  for j in range(len(input_list)):

    if input_list[j] % factor != 0:
      flag = False

  return flag


def getting_shorter(input_list : list[str]) -> bool:

  '''
  Checks if all of the strings in the given list are decreasing ir order by length

  >>> getting_shorter(['fore', 'gave', 'sam', 'to'])
  False

  >>> getting_shorter(['largest', 'large', 'big', 'ok'])
  True

  >>> getting_shorter(['largest', 'largestbiggest', 'big', 'ok'])
  False

  >>> getting_shorter(['123', '12', '1', ''])
  True

  >>> getting_shorter(['abcdefgh', 'abcdefg', 'abcdef', 'abcde'])
  True
  '''

  flag = True

  for i in range(len(input_list) - 1 ):

    if (len(input_list[i]) > len(input_list[i+1])):
      flag = True

    else:
      return False

  return flag

