def external_function(x):
    a = 10
    def inner_function():
        return x * a
    res = inner_function()
    print(res)
    return inner_function


x = 5
external_function(x)