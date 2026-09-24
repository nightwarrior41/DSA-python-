# Brute force way of finding the factors of a given number
#Going throug all the numbers
# def Brute_fact(num):
#     result = []
#     for i in range(1,abs(num+1)):
#         if num%i == 0:
#             result.append(i)
#     return result

# #Going through half the numbers
# def better_fact(num):
#     result = []
#     for i in range(1,abs(num//2)):
#         if num%i == 0:
#             result.append(i)
#     result.append(num)
#     return result

#The optimal way of finding the factors of a given number

def fact(num):
    '''
    It is an optimal way of finding factors of a given number.
    This method offers a way that can assess the factors of a given number in O(sqrt(n)) !
    here we go through the sqrt(num) to finds its factor !!
    here if k is an factor of num and  k*i == num then i is also an factor of it !
    '''
    import math as m
    result = []
    for i in range(1,int(m.sqrt(abs(num)))+1):
        if num%i == 0:
            result.append(i)
            if (num//i) != i:
             result.append(int(num//i))
    result.sort()
    return result

if __name__=='__main__': 
   print(fact(36),help(fact))
    