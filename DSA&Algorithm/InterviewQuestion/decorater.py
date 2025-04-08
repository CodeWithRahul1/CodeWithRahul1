def decoratore_method(f):
    def wrapper(x, y):
        res = f(x, y)
        multi = x * y
        print(f"Multiplication inside decorator: {multi}")
        return res
    return wrapper

@decoratore_method
def method(x, y):
    return x + y

print("Sum:", method(5, 6))