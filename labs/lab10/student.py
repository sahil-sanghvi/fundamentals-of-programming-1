import doctest

class Student:
    """ Student with unique id (sid) and current grade (grade)"""

    def __init__(self, sid: str, grade: int) -> None:
        """ initializes an instance of a Student with sid and grade
        >>> stdnt = Student('V00123456', 89)
        """
        self.__sid = sid
        self.__grade = grade

    def __str__(self) -> str:
        """ return a formatted string with sid and grade of self Student
        >>> stdnt = Student('V00123456', 89)
        >>> str(stdnt)
        'V00123456: 89/100'
        """
        return f'{self.__sid}: {self.__grade}/100'

    def __repr__(self) -> str:
        """ return a formatted string  with student attributes
        >>> stdnt = Student('V00123456', 89)
        >>> stdnt
        Student('V00123456', 89)
        """        
        return f'Student({repr(self.__sid)}, {repr(self.__grade)})'
    
    def __eq__(self,other:'Student') -> bool:
        """ 
        returns True if sid of self and other are equal
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt1_eq = Student('V00123456', 89)
        >>> stdnt1_noteq = Student('V00123457', 89)
        >>> stdnt1 == stdnt1
        True
        >>> stdnt1 == stdnt1_eq
        True
        >>> stdnt1 == stdnt1_noteq
        False
        
        """
        student1 = self.__sid
        student2 = other.__sid
        
        if student1 == student2:
            return True
        
        else:
            return False
                
    
    
    # TODO: add documentation for these instance methods
    def get_sid(self):
        '''
        Getter function to obtain the sid of the student
        
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt2 = Student('V00123456', 99)
        >>> stdnt3 = Student('V00123457', 59)
        
        >>> stdnt1.get_sid()
        'V00123456'
        
        >>> stdnt2.get_sid()
        'V00123456'
        
        >>> stdnt3.get_sid()
        'V00123457'
        
        '''
        return self.__sid

    def get_grade(self):
        '''
        Getter function to obtain the grade of the student
        
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt2 = Student('V00123456', 99)
        >>> stdnt3 = Student('V00123457', 59)
        
        >>> stdnt1.get_grade()
        89
        
        >>> stdnt2.get_grade()
        99
        
        >>> stdnt3.get_grade()
        59
        
        '''        
        
        return self.__grade

    def set_grade(self, grade):
        '''
        Setter function to set the sid of the student
        
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt2 = Student('V00123456', 99)
        
        >>> stdnt1.set_grade(78)
        >>> stdnt1.get_grade()
        78 
        
        >>> stdnt2.set_grade(89)
        >>> stdnt2.get_grade()
        89 
        
        '''
        
        self.__grade = grade
        
    def is_grade_above(self,threshold:int) -> bool:
        '''
        Function to check if the grade of the student is above a particular threshold
        
        >>> stdnt1 = Student('V00123456', 89)
        >>> stdnt2 = Student('V00123456', 99)
        
        >>> stdnt1.is_grade_above(78)
        True 
        
        >>> stdnt2.is_grade_above(100)
        False 
        '''
        
        if self.get_grade() > threshold:
            return True
        
        else: return False
    
