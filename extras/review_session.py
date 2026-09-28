import math
import doctest

""" Welcome to the CSC 110 final exam review session run by Women in Engineering and Computer Science (WECS) in collaboration with IEEE!
Instagram: @uvicwecs

The following questions are for practice only and are not representitive of the format or specific content of the final exam. This review session is run by upper-year students who know the material well, but your professors are experts in their field. If we say anything that contradicts your professor, listen to your professor!
"""

# OPERATIONS 
""" What will be the output of the following operations?
Try to figure it out on your own and then try it in the shell to see if you were right!

a) 6/2

b) 7/2

c) 13//2

d) 18%5

Some more complicated examples:

e) 57 % 10/4 + 1.25 * 4

f) 5 * 6 / 4 % 3 - 23 / (14 % 6)

g) (6.7 > 25) and 9 > 2 and not (8.2 < 5)

h) (6.7 > 25) or 9 < 2 or not (8.2 < 5)

i) "17" + "4"

"""

# CODE TRACING  
""" A code tracing question! What will the output be for each of the following inputs?

a) if_else(5, 5 -> 16 5

b) if_else(18, 4) -> 2 6

c) if_else(3, 6) -> 5 8

"""
def if_else(x, y):
    if x==y:
        x += 11
    elif x > 2*y:
        x = 0
    if x==0 or y>x:
        x += 2
        y += 2
    
    print(x,y)
    

""" The following code will have 4 lines of output. Trace the code to predict the output then run the code to see if you were right.
BE VERY CAREFUL, this question is tricky. Draw out what is happening. I will go over this question in detail on the board.
"""
def caller():
    y = 1
    x = 3
    a = [0, 0, 0, 0]
    
    mystery(a, y, x)
    print(x, y, a)
    
    x = y - 1
    mystery(a, y, x)
    print(x, y, a)
    
def mystery(a, x, y):
    if x < y:
        x+=1
        a[x] = 17
    else:
        a[y] = 10
        
    print(x, y, a)
    
"""
Output: 
2 3 [0, 0, 17, 0]
3 1 [0, 0, 17, 0]
1 0 [10, 0, 17, 0]
0 1 [10, 0, 17, 0]

Here the array changes because an array's value can be referenced to and changed in some other function but its value will be updated in the function it was made in too.

"""

""" What is the output of the following function?
Trace the output yourself and then run the code to see if you were right.
"""
def counter_output():
    max_val = 17
    counter = 0
    
    while(counter < max_val):
        print("counter is: " + str(counter))
        counter += 5


""" What will be the value of x after this code has excecuted?"""

def x_value():
    x=0
    for i in range(-2, 3):
        for j in range(20, 10, -1):
            x+=1
    print(x)


# CODE WRITING        
""" Starting with the following code, print the numbers from 100 to 1. You CANNOT change the code provided.
"""
def print_from_100():
    #some_number = choose the right value!
    counter = 100
    for i in range(0, 100):
        print(counter)
        counter -= 1
        
""" Rewrite the following for loop as a while loop.
"""
def for_loop():
    """
    for i in range(10, -1, -1):
        print(i)
    """
    i = 10
    while i > -1:
        
        print(i)
        i -= 1
        
""" The following code has 2 syntax errors and 1 logic error, fix these errors such that the output will be all odd numbers from 0 to 9 inclusive.

def syntax_logic():
    for i in range(0, 9):
        if i%2 = 1
            print(i)
"""       

def syntax_logic():
    
    for i in range(0,10):
        if i%2 == 1:
            print(i)
 
""" Write a function called is_sorted that accepts a list of floats and returns True if the list is in sorted (nondecreasing) order and False otherwise.
Assume the list has length of at least 1, and a list with exactly 1 element should return True.

list1 = [16.1, 12.3, 22.2, 14.4]
is_sorted(list1) should return False

list2 = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]
is_sorted(list2) should return True
"""
def is_sorted(input_list: list[float]) -> bool:
    
    if len(input_list) == 1:
        return True
    
    
    
    for i in range(1,len(input_list)):
        
        if input_list[i] < input_list[i-1]:
            return False

    return False

""" Write a function called count_in_range that accepts 3 arguments: a list of integers, a minimum value (an integer), and a maximum value (an integer).
The function will return a count of the number of array elements whose values fall between the minimum and maximum INCLUSIVE.

Example:
some_list = [14, 1, 22, 17, 36, 7, -43, 5]
count_in_range(some_list, 4, 17) should return 4
"""
def count_in_range(lst: list[int], mini: int, maxi: int):
    
    counter = 0
    
    for num in lst:
        
        if num >= mini and num <= maxi:
            counter += 1
            
    return counter

""" Write a function called count_duplicates that accepts a SORTED list of integers and returns the number of duplicate elements in the list.
The list passed as an argument is guaranteed to be in sorted order.

my_list = [1, 2, 3, 3, 8, 8, 8, 8, 11, 11, 11, 14, 19, 19]
count_duplicates(my_list) would return 7 since there is 1 duplicate of 3, 3 duplicates of 8, 2 duplicates of 11, and 1 duplicate of 19.
"""
def count_duplicates(sorted_list):
    count = 0
    
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] == sorted_list[i + 1]:
            count += 1
    
    return count




# DICTIONARY + FILES
""" The following question is taken directly from CSC 110 lecture materials. I think it's a great example that you should understand well and be able to solve fairly easily at this point. (but if not, this is your chance to learn!)
"""
"""
a) Design a function that will take a filename of a file with rows of names and email addresses separated by commas and creates and returns a dictionary of email contacts. If name already exists in the dictionary, overwrite it with the new email.
You can test this by printing each key-value pair and using the emailInfo.csv document.
"""

def contact(filename: str) -> dict:
    
    file = open(filename,'r')
    lines = file.readlines()
    
    email_dict = {}
    
    for line in lines:
        
        current_line = line.split(',')
        
        name = current_line[0]
        email = current_line[1].strip()
        
        email_dict[name] = email
        
    return email_dict

"""
b) Design a function that takes a filename of a file with rows of votes containing a voter id followed by vote (yes, no or abstain) and returns a dictionary containing the counts of votes for yes, no, abstain.
You can test this by printing each key-value pair and using the votes.txt document.
"""

"""
c) Design a function that takes a text file and creates and returns a dictionary of all the words in the file (no duplicates) followed by the number of times that word occured.
You can test this by printing each key-value pair and using the small.txt or happy.txt documents.
"""


#CLASSES
""" Create a class called Point. 
Write the __init__ function to initialize the x and y coordinates of Point. If no values are given then x and y should be initialized to 0.

Write the __repr__ function such that the output would be formatted like this:
p1 = Point(1,2)
print(p1) should print: Point(1, 2)

Write a translate(dx, dy) function which returns a new Point with x and y coordinates shifted by dx and dy respectively.
"""

""" Create a class called Rectangle. 

Write the __init__ function to initialize the upper_right and lower_left Points of our Rectangle. If no Points are given then upper_right and lower_left should be initialized to Point(0,0).

Write the __repr__ function such that the output would be formatted like this:
r1 = Rectangle(Point(1,2), Point(0, 0))
print(r1) should print: The upper_right point is at (1, 2) and the lower_left point is at (0, 0).

Write an area function which returns the area of the Rectangle.

Write a translate(dx, dy) function which returns a new Rectangle where the upper_right and lower_left Points are both translated by dx and dy.
r2 = Rectangle(Point(5,3), Point(1, 2))
r2.translate(1, 3) should return:
The upper_right point is at (6, 6) and the lower_left point is at (2, 5).
"""


# COMMON ERRORS
""" Fix the following code so that it will catch index errors. If there is an IndexError, print "there was an index error".

if we call index_error(2, [1, 2, 3]) the output should be:
3
there was an index error
"""
def index_error(value, my_list):
    for i in range(value, value*2):
        print(my_list[i])

""" What is the output of the following function calls?

a) test_errors('0')

b) test_errors('-1')

c) test_errors('10')

d) test_erros('garlic')

"""
def test_errors(val):
    try:
        val = int(val)
        val += 1
        x = 10 / val
        print("A")
    except ZeroDivisionError:
        print("B")
    except TypeError:
        print("C")
    except ValueError:
        print("D")  