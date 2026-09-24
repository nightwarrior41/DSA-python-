# Iterative way

def facti(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact

# print(facti(5))

# Recursive way

def factr(num):
    if num == 0 or num == 1:
        return 1
    if num < 0:
        return -1
    return num*factr(num-1)

print(factr(10))