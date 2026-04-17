myvar = 10 # global variable

def myfun():
    myvar = 20 # local variable
    print(myvar)
# global variable can be accessed inside using the global keyword followed by variable name.

myfun()
print(myvar)
