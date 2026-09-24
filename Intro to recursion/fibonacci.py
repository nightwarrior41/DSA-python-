# The recrusive way of printing nth fibonacci number
def fibo_r(n):
    if n==0 or n==1:
        return n
    return fibo_r(n-1) + fibo_r(n-2)

print(fibo_r(5))

# The iterative way
def fibo_i(n):
    if n==0 or n==1:
        return n
    prev1 = 0 ; prev2 = 1 ; fib=0
    for i in range(1,n):
        fib = prev1+prev2
        prev1 = prev2
        prev2 = fib
  
    return fib

print(fibo_i(5))