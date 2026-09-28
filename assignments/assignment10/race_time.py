import doctest
class RaceTime:
    """ RaceTime: represents a race time result in 
    milliseconds (ms), seconds (sec), minutes (mins)
    Precondition, ms, sec, mins>=0, ms<1000, sec<60
    """

    def __init__(self, ms: int, sec: int, mins: int) -> None:
        """ initializes attributes of RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        """
        self.__ms = ms
        self.__sec = sec
        self.__mins = mins

    def get_ms(self) -> int:
        """ returns ms of self RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        >>> rt.get_ms()
        88
        """
        return self.__ms

    def get_sec(self) -> int:
        """ returns sec of self RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        >>> rt.get_sec()
        20
        """
        return self.__sec

    def get_mins(self) -> int:
        """ returns mins of self RaceTime instance
        >>> rt = RaceTime(88, 20, 4)
        >>> rt.get_mins()
        4
        """
        return self.__mins

    def __str__(self) -> str:
        """ returns a readable string with ms, sec, mins of RaceTime
        >>> rt = RaceTime(88, 20, 4)
        >>> str(rt)
        '4:20:88'
        """
        return f'{self.__mins}:{self.__sec}:{self.__ms}'

    def __repr__(self) -> str:
        """ returns a string representation of self RaceTime
        >>> rt = RaceTime(88, 20, 4)
        >>> repr(rt)
        'RaceTime(88, 20, 4)'
        """
        return f'RaceTime({self.__ms}, {self.__sec}, {self.__mins})'

    def __eq__(self, other: 'RaceTime') -> bool:
        """ returns True if self RaceTime has same ms, sec, mins as
        other RaceTime, otherwise False
        >>> rt121920a = RaceTime(12, 19, 20)
        >>> rt121920b = RaceTime(12, 19, 20)
        >>> rt121921  = RaceTime(12, 19, 21)
        >>> rt121820  = RaceTime(12, 18, 20)
        >>> rt111920  = RaceTime(11, 19, 20)

        >>> rt121920a == rt121920a
        True
        >>> rt121920a == rt121920b
        True
        >>> rt121920a == rt121921
        False
        >>> rt121920a == rt121820
        False
        >>> rt121920a == rt111920
        False
        """
        return (self.__ms == other.get_ms()
                and self.__sec == other.get_sec()
                and self.__mins == other.get_mins())

    def is_faster(self,other:"RaceTime") -> bool:
        '''
        This function compares two instances of RaceTimee and returns a boolean contraining if the self instance is faster or not.
        
        >>> race1 = RaceTime(12, 20, 25)
        >>> race2 = RaceTime(12, 19, 20)
        >>> race3  = RaceTime(12, 19, 21)
        >>> race4  = RaceTime(12, 19, 21)
        >>> race5  = RaceTime(11, 19, 20)

        >>> race1.is_faster(race2)
        False
        
        >>> race2.is_faster(race1) 
        True
        
        >>> race3.is_faster(race4)
        False
        
        >>> race5.is_faster(race1) 
        True
        
        >>> race1.is_faster(race5)
        False
        '''
        
        if self.__mins == other.get_mins():
            if self.__sec == other.get_sec():
                if self.__ms < other.get_ms():
                    return True
                else:
                    return False
            else:
                if self.__sec < other.get_sec():
                    return True
                else: 
                    return False
                
        else:
            if self.__mins < other.get_mins():
                return True
            else:
                return False
    