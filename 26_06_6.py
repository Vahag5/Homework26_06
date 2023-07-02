x = 10
def my_function():
    x = 20
    print(x)  # 20
    print(globals()['x']) #10

my_function()
