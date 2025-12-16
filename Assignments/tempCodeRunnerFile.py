def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
    
def hello():
    print("hello")
@my_decorator
def hello():
    print("hello")