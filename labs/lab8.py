import doctest

Person = tuple[str, int]
NAME = 0
AGE = 1


def file_to_person_list(file_name : str) ->  list[tuple]:
  
  '''
  this function takes the name of a valid existing file as an argument and reads 
  the lines of text from a file that contains, on each line: the name of a 
  person and their age as a whole number separated by a space. it creates 
  and returns a list of tuples, where each tuple contains the name of a person and their age.
  
  >>> filename = 'lab8-name-age.txt'
  >>> file_to_person_list(filename)
  [('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)]
  
  >>> filename = 'empty-lab8-name-age.txt'
  >>> file_to_person_list(filename)
  []
   
  
  '''
  #initialising the output list to be an empty list
  output_list = []
  
  
  #opening the file and passing it "r" which reads all the lines and returns a list
  file = open(file_name, "r")
  lines = file.readlines()

  for x in range(len(lines)):
    current_line = lines[x].split()
    
    name = current_line[NAME]
    age = int(current_line[AGE])

    person = Person([name, age])
    output_list.append(person)

  #closing thr file and returning the output list   
  file.close()  
  return(output_list)



def get_average_age(person_list : list[Person]) -> int:
  '''
  this function takes a list with person information tuples and calculates and returns the average age of all ages in the list as a whole number (rounded down).
  precondition person_list != []
  
  >>> lst = [('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)]
  >>> get_average_age(lst)
  31
  
  >>> lst = []
  >>> get_average_age(lst)
  0
  
  '''
  
  #initialising the total to be 0
  total = 0
  ages_no = len(person_list)
  
  #for loop that adds that acesses the AGE in every tuple and add its value to the total
  for i in range(ages_no):
    total += person_list[i][AGE]
    
  
  if ages_no == 0:
    return 0
  
  
  average = total/ages_no
    
  #returning the total
  return int(average)


  
def get_above_age(person_list : list[Person], threshold : int) -> list[Person]:
  '''
  this function takes a list with person information tuples and a threshold age and creates and returns a list of all the person information tuples that have an age older than the threshold age.
  
  >>> lst = [('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)]
  >>> get_above_age(lst,31)
  [('Jose', 53), ('Rajan', 65)]
  
  >>> lst = [('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)]
  >>> get_above_age(lst,100)
  []
  
  '''
  
  #initialising the output list to be an empty list
  output_list = []
  
  #for loop that acesses AGE in every person tuple
  for i in range(len(person_list)):
    
    #if statement that checks if the AGE acessed is greater than the threshold
    if person_list[i][AGE] > threshold:
      output_list.append(person_list[i])
  
  #returning the output list    
  return(output_list)



def to_file(person_list : list[Person], file_name : str) -> None:
  '''
  this function takes a list with person information tuples and the name of a file as arguments and writes the name and age from each tuple on its own line with the name and age separated by commas.
  
  >>> lst = [('Claire',21)]
  >>> output_file = 'lab8-output.csv'
  >>> to_file(lst,output_file)
  '''
  
  #opening the file and passing it "w" which writes in the list
  file = open(file_name, "w")
  
  for i in range(len(person_list)):
    
    #writing the person's anem and age in the file
    file.write(str(person_list[i][NAME]) + ',')
    file.write(str(person_list[i][AGE]) + '\n')
  
  #closing the file
  file.close()


def write_names_above_avg_age(input_file : str, output_file : str) -> None:
  '''
  this function takes the names of the people above the average age and adds it to a csv file
  
  >>> write_names_above_age_age(lab8-name-age.txt,above-age.csv)
  '''
  
  #passing the input list the file_to_person_list function
  input_list = file_to_person_list(input_file)
  
  if len(input_list) != 0:
    average_age = get_average_age(input_list)
    output_list = get_above_age(input_list, average_age)
  
    #passing the variables output list and output file to the to_file function
    to_file(output_list, output_file)
  else:
    output_list = []
    to_file(output_list,output_file)