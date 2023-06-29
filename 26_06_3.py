import math
def calculate_area(r):
    if type(r) != float and type(r) != int: 
        raise TypeError
    s =  math.pi * (r**2)

    print(s)
    return s

r = 10
calculate_area(r) #  314.1592653589793








