def my_decorator(param_function):
    def wrapper():
        print("Decorator starting")
        param_function()
        print("Decorator ending")
    return wrapper

