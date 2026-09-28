import doctest

def print_racoon():
    
    """
    This function prints out a ascii art which represents a racoon
    
    >>> print_racoon()   
    """
    
    print('  /\_/\\')
    print(' ( o\'o )')
    print(' > "^" <')
    print('|w____w|')

def print_crab():
    
    """
    This function prints out a ascii art which represents a crab
    
    >>> print_crab()
       
    """    
    
    print('                                   _ _ _ _ _ _ ')
    print(' _ _ _ _ _ _ _ _                  /  _\'_\'_\'_\'_ \\')
    print('>_\'_\'_\'_\'_\'_\'_  \      m  m      /  /         \\ \\ ')
    print('              \  \_____|__|_____/  /           \\ \\')
    print('              (                    )           //\\\\  ')
    print('              (                    )          // \'\\\\')
    print('              (        \'\"\"\'        )         //   \'\\\\')
    print('                / _____    _____  |          V	  \' V')
    print('               / /    / /\\ \\    \\ \\        ')
    print('              / /    / /  \\ \\    \\ \\       ')
    print('              \'V\'    \'V\'   \'V\'    \'V\'')
    
    
def print_logo():
    
    """
    This function prints out two ascii art logos created in two functions named print_racoon() and print_crab() with a spacer line in between
    
    >>> print_logo()
    
    """
    
    print('/~~~~~~~~\\')
    print_racoon();
    print('/~~~~~~~~\\')
    print_crab();
    print('/~~~~~~~~\\')
    print_racoon();
    print('/~~~~~~~~\\')
    print_crab();
    print('/~~~~~~~~\\')
    
    

PI = 3.14

def calculate_surface_area(height: int, diameter: int):
    
    '''
    The following functions calculates and prints the surface area of a cylinder. The user needs to input the height and diameter as arguments.
    
    The first argument is the height and the second argument is the diameter
    >>> calculate_surface_area(1.2, 3.5)
    cylinder area: 32.4
    '''
    
    
    # calculates the radius using the diameter
    radius = (diameter/2)
    
    # calculates the circumference 
    circumference = 2 * PI * radius
    
    # calculates the top surface area
    cylinder_top_area = 2 * PI * (radius**2)
    
    # calculates the curved surface area
    cylinder_curved_area = circumference * height
    
    # calculates the total area which is the sum of the two tops of the cylinder and the curved walls of the cylinder
    
    total_area = cylinder_top_area + cylinder_curved_area 
    
    # prints the total area for the user
    print(f'cylinder area: {total_area:.1f}')
