import doctest

# PART 1

#1
def get_sequence(a: int, b:int, ending:int) -> str:
    
    '''
    This function takes the starting value and ending value along with the increment value and returns a string with the elements of the sequence
    
    >>> get_sequence(2, 5, 32)
    '2,7,12,17,22,27,32'
    
    >>> get_sequence(2, 5, 37)
    '2,7,12,17,22,27,32,37'
    
    >>> get_sequence(2, 5, 31)
    '2,7,12,17,22,27'
    
    >>> get_sequence(6,10,100)
    '6,16,26,36,46,56,66,76,86,96'
    
    '''
    
    sequence = ''
    count = 0
    counter = 0
    
    for i in range(a,ending + 1,b):
        count += 1
    
    for i in range(a,ending + 1,b):
        
        counter = counter + 1
        
        if counter == count :
            sequence = sequence + str(i)
        else:    
            sequence = sequence + str(i) + ','
            
        
            
    return sequence

#2
def digit_sum(n:int) -> int:
    
    '''
    This function takes one number as an argument and returns the sum of the digits of the number
    
    >>> digit_sum(0)
    0
    
    >>> digit_sum(432)
    9
    
    >>> digit_sum(-571)
    13
    
    '''
    
    n = abs(n)
    digi_sum = 0
    
    while n != 0:
        
        rem = n % 10
        digi_sum = digi_sum + rem
        
        n //= 10
        
    return digi_sum

#3
def sum_factors(n: int) -> str:
    
    '''
    This function takes an integer argument and returns the sum of factors of that number
    
    >>> sum_factors(12)
    16
    
    >>> sum_factors(60)
    108
    
    >>> sum_factors(0)
    0
    
    '''
    
    sum_factor = 0
    
    for x in range(1,n):
        
        if n % x == 0:
            
            sum_factor += x
                
    return sum_factor

#4
def is_perfect(n:int) -> bool:
    
    '''
    This function determines if the number entered as a function argument is a perfect number or not
    
    By definition, a perfect number is a positive integer that is equal to the sum of its positive divisors.
    
    >>> is_perfect(28)
    True
    
    >>> is_perfect(496)
    True
    
    >>> is_perfect(0)
    False
    
    >>> is_perfect(-123)
    False
    '''

    if n <= 0:
        return False
    
    if n == (sum_factors(n)):
        return True
    
    return False
#5
def n_perfect_numbers(n:int) -> str:
    
    '''
    This function takes a value n and returns a string of the first n perfect numbers 
    
    >>> n_perfect_numbers(0)
    ''
    
    >>> n_perfect_numbers(1)
    '6'
    
    >>> n_perfect_numbers(4)
    '6,28,496,8128'
    
    >>> n_perfect_numbers(-3)
    '6,28,496'
    
    '''
    
    n = abs(n)
    
    count = 1
    i = 0
    str_perfect = ''
    
    if n == 0:
        return str_perfect
    
    while count != n+1 :
        
        if is_perfect(i):
            count += 1
            
            if count == (n+1):
                str_perfect = str_perfect + str(i)
                
                return str_perfect
    
            else:
                str_perfect = str_perfect + str(i) + ','
                
    
            
        i += 1
                        
# PART 2

import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5


def roll_one_die() -> int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    # this line MUST be uncommented when submitting to PrairieLearn
    die = random.randint(MIN_ROLL, MAX_ROLL)

    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # this line MUST be commented out when submitting to PrairieLearn
    # die = int(input('enter a simulated dice roll\n'))

    return die

#1

def take_turn(player_name : str, current_points : str, round_no : int) -> int:

    '''
    This fucntion takes three arguments being player name, current player points and round number which is also the target value which has to be between 1 and 6
    '''

    turn_value = False
    dice_roll = [0,0,0]

    total_round_points = current_points

    # Prints details : player's name and round number
    print(f'Player {player_name} is taking a turn in round {round_no}')

    while turn_value == False:

        dice_roll[0] = roll_one_die()
        dice_roll[1] = roll_one_die()
        dice_roll[2] = roll_one_die()

        # Prints dice roll values
        print(f'Three dice rolled: {dice_roll[0]}, {dice_roll[1]}, {dice_roll[2]}')

        check_dice_value = 0
        current_total_round_points = 0

        for i in range(0, 3):

            if dice_roll[i] == round_no:
                check_dice_value += 1

        if check_dice_value == 3:
            current_total_round_points = 21

        elif check_dice_value == 2:
            current_total_round_points = 2
        
        elif check_dice_value == 1:
            current_total_round_points = 1
        
        # Checks if all the dice rolls have the same value and gives player 5 points
        elif (dice_roll[0] == dice_roll[1] == dice_roll[2]):
            current_total_round_points = 5
        
        else:
            current_total_round_points = 0
            
        # Prints score of each round
        if total_round_points > 0:
            print(f'scored: {current_total_round_points} points')
            
        else:
            print(f'scored: {current_total_round_points} point')
            
        total_round_points += current_total_round_points
            
        # Prints total score
        print(f'Total points: {total_round_points}')
        print()
            
        # Ends roll if zero points were earned
        if current_total_round_points == 0 or total_round_points >= 21:
            turn_value = True

    return total_round_points


def play_round(p1 : str, p2 : str, round_no : int) -> str:

    '''
    This functions plays rounds of Bunko with two players till one of the players get a score of 21 or above. The function will alternate turns starting with the first player until one of the players reaches at least 21 points. The round should stop immediately when a player reaches 21, not allowing the other player to have another turn.
    '''
  
    # Creating two lists for keeping a record of  player names and scores
    player_name = [p1, p2]
    player_total_points = [0,0]
    
    winning_player = ''
  
    # Variable to decide if round is over or not, and increment variable
    round_status = True
    i = 0
  
    while round_status == True:
  
        # running a for loop which will iterate two times for the two players
        for i in range(0,2):
  
            if round_status == True:
                player_total_points[i] = take_turn(player_name[i], player_total_points[i], round_no)
  
            # Checks if total is above 21, if its above 21, ends both loops
            if player_total_points[i] >= 21:
                print(f'the winner of this round is: {player_name[i]}')
                winning_player = player_name[i]
                round_status = False
  
    # Prints final text output
    print(f'{p1} has {player_total_points[0]} points and {p2} has {player_total_points[1]} points')
  
    return winning_player
