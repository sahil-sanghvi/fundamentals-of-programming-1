from race_time import RaceTime
import doctest
class RaceResult:
    """ RaceResult: represents a racer's result with 
    name, country and race finish time
    """

    def __init__(self, name: str, country: str, finish_time: RaceTime) -> None:
        """ initializes attributes of RaceResult instance
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        """
        self.__name = name
        self.__country = country
        self.__finish_time = finish_time

    
    def __eq__(self,other:"RaceResult") -> bool:
        '''
        returns True if self RaceResult has same name, country, race time as
        other RaceResult, otherwise False
        
        >>> rt121920b = RaceTime(12, 19, 20)
        >>> rt121920c = RaceTime(12, 19, 20)
        >>> racer1 = RaceResult('Sahil','India',rt121920b)
        >>> racer2 = RaceResult('Sahil','India',rt121920c)
        >>> racer1 == racer2
        True
        
        >>> rt121920b = RaceTime(12, 19, 25)
        >>> rt121920c = RaceTime(12, 19, 20)
        >>> racer1 = RaceResult('Sahil','India',rt121920b)
        >>> racer2 = RaceResult('Sahil','India',rt121920c)
        >>> racer1 == racer2
        False
        
        >>> rt121920b = RaceTime(12, 19, 20)
        >>> rt121920c = RaceTime(12, 19, 20)
        >>> racer1 = RaceResult('Lihas','India',rt121920b)
        >>> racer2 = RaceResult('Sahil','India',rt121920c)
        >>> racer1 == racer2
        False
        
        '''
        
        return (self.__name == other.get_name()
                and self.__country == other.get_country()
                and self.__finish_time == other.get_finish_time())
        
    
    
    def get_name(self) -> str:
        """ returns name of self RaceResult instance
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        >>> racer.get_name()
        'Usain Bolt'
        """
        return self.__name

    def get_country(self) -> str:
        """ returns country of self RaceResult instance
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        >>> racer.get_country()
        'Jamaica'
        """
        return self.__country

    def get_finish_time(self) -> RaceTime:
        """ returns RaceTime of self RaceResult instance
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        >>> racer.get_finish_time()
        RaceTime(12, 19, 9)
        """
        return self.__finish_time

    def __str__(self) -> str:
        """ returns a readable string with name, country, finish_time 
        of RaceResult
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        >>> str(racer)
        'Usain Bolt is from Jamaica. Finish Time: 9:19:12'
        """
        result_str = f'{self.__name} is from {self.__country}. ' \
            + f'Finish Time: {self.__finish_time}'
        return result_str

    def __repr__(self) -> str:
        """ returns a string representation of self RaceResult
        >>> rt = RaceTime(12, 19, 9)
        >>> racer = RaceResult('Usain Bolt', 'Jamaica', rt)
        >>> repr(racer)
        "RaceResult('Usain Bolt', 'Jamaica', RaceTime(12, 19, 9))"
        """
        result_str = f'RaceResult({repr(self.__name)}, ' \
            f'{repr(self.__country)}, {repr(self.__finish_time)})'
        return result_str
