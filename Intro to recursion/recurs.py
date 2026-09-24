#head recursion
def greetH(count):
    if count < 1:
        return 
    greetH(count-1) # Here call stack build first then it prints
    print("Hi")
    
    
# Tail Recursion
def greetT(count):
    if count < 1:
        return
    print('Hi') # here function prints first then build the stack
    greetT(count-1)
    
greetT(4)