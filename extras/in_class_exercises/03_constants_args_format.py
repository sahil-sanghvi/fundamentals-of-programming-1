
def acres_to_sqr_meters():
    acres = 5.7

    sqr_meters = acres * 4046.85642
    print('Area is: ', sqr_meters, 'm^2')


'''
Q1a. The function definition above is a solution to the problem I left you
with at the end of last lecture.
How can we make this function easier for some reading it to quickly
comprehend what the function does?
'''


'''
Q1b. The acres_to_sqr_meters function is not very versatile -
it will only calculate the square meters for 5.7 acres!
Edit the function so that it will calculate the square meters
for ANY non-negative number of acres.
'''


'''
Q2. Design a function that will take the name of the best team and
print out a cheer for that team.
'''

def team_cheer(team:str):
    '''
    This function will print out a cheer of the name of the team entered and print it out
    
    >>> team_cheer('Sahil')
    East or West Sahil is the best
    
    '''
    
    print(f'East or West {team} is the best')


'''
Q3. Design a function called print_bill that takes the
price of a clothing item. The function should print the bill
which should include the following items:
 the price, the PST amount, the GST amount, and the total bill including taxes
NOTE: PST is provincial sales tax at 7%
      GST is goods and services tax at 5%
'''
PST_value = 0.07
GST_value = 0.05

def print_bill(price:float):
    '''
    This function takes the input as the price of the clothing and prints out the price, the PST and GST amount and the total bill including the two taxes.
    
    NOTE: PST is provincial sales tax at 7%
          GST is goods and services tax at 5%
          
    >>>   print_bill(100)
          The price of the item is 100 
          PST: $7.000000000000001 
          GST: $5.0 

         Total bill amount: $112.0
      
    '''
    
    PST = PST_value * price;
    GST = GST_value * price;
    
    total_price = PST + GST + price;
    
    print(f'The price of the item is ${price:.2f} \n PST: ${PST:.2f} \n GST: ${GST:.2f} \n')
    print(f'Total bill amount: ${total_price:.2f}')
    



'''
Q4. Design a function that will take a person's name and age and will
print a personalized message for that person.
For example, if we call the function as: welcome('Amy', 21)
the function should print:  Welcome Amy! Amy's 21 years old.
'''
