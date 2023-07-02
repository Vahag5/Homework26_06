def external_function(x):
    a = 10
    def inner_function():
        result = x * a
        return result
    result = inner_function()
    print(result)

x = 5
external_function(x)
