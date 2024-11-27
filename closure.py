# Closure
# A function that returns another function
# The returned function retains a copy of the scope of the outer function

def greet(name):
    print('Hello')

    def display_name():
        print(name)

    return display_name


spam = greet('John')
spam()

