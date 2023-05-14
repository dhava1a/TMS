def announce(func):
    def wrapper():
        print("About to run the function...")
        func()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, World!")

hello()