import doctest
from student import Student
#import student
def get_students(filename: str) -> list[Student]:
    '''
    This function takes a filename and returns a list of Student type in which the first element is the sid and the second element is the grade
    
    >>> get_students('student_data.csv')
    [Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)]
    
    >>> get_students('empty.csv')
    []
    
    '''
    
    
    file = open(filename,'r')
    lines = file.readlines()
    output_list = []
    
    if len(lines) == 1:
        return output_list
    
    for line in lines:
        
        current_line = line.split(',')
        current_line[1] = current_line[1].strip()
        
        student1 = Student(current_line[0],int(current_line[1]))
        
        output_list.append(student1)
        
    return output_list


def get_classlist(student_name: list[Student]) -> list[str]:
    
    '''
    This function takes a list of student instances and returns a new list with only student sids 
    
    >>> lst = [Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)]
    >>> lst2 = []
    
    >>> get_classlist(lst)
    ['V00123456', 'V00123457', 'V00123458', 'V00123459']

    >>> get_classlist(lst2)
    []
    '''
    output_list = []
    
    if student_name == []:
        return output_list
    
    
    for stu in student_name:
        
        stu_name = stu.get_sid()
        
        output_list.append(stu_name)
        
    return output_list

def count_above(student_name: list[Student],threshold:int) -> int:
    
    '''
    This function returns the number of students which have a grade above the threshold given
    
    >>> lst = [Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)]
    >>> lst2 = []
    
    >>> count_above(lst,80)
    2
    
    >>> count_above(lst,90)
    1
    
    >>> count_above(lst,100)
    0
    
    >>> count_above(lst,0)
    4
    
    >>> count_above(lst2,90)
    0
    
    '''
    num_student = 0
    
    if student_name == []:
        
        return num_student
    
    for stu in student_name:
        
        
        if stu.is_grade_above(threshold):
            num_student += 1
    
    
    return num_student


def get_average_grade(student_name: list[Student]) -> float:
    '''
    This function returns a floating point which is the average of the overall grades gained by the students
    
    >>> lst = [Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)]
    >>> lst2 = []
    
    >>> get_average_grade(lst)
    74.0
    
    >>> get_average_grade(lst2)
    0
    
    '''
    
    avg_grade = 0
    len_stu = len(student_name)
    if student_name == []:
        return avg_grade
    
    for stu in student_name:
        
        stu_grade = int(stu.get_grade())
        avg_grade += stu_grade
        
    avg_grade = avg_grade/len_stu
    
    return avg_grade


s = [1,2,3,4]
a = [7,8,9,10]
d = s+a

print(d)
