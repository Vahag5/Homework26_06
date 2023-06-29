x = 10
def my_function() :
    x = 20
    print(x)
    global x
    print(x)


my_function() # SyntaxError: name 'x' is used prior to global declaration
