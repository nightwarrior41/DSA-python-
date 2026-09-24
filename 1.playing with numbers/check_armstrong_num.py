def count_digits1(num):
    count = 0;n = abs(num)
    while n > 0:
        count+=1
        n//=10
    return count
        

def check_armstrong(num):
    n = abs(num)
    total = 0
    length = len(str(n)) # python way or count_digit1(num)
    if length == 1 :
        return True
    else:
        while n > 0:
            total += (n%10)**length
            n //=10
        return total == num


def list_of_armstrong_num(lim):
    l = []
    limit = lim
    i = 100000 ; j=0
    while lim:
       if j < i: 
          if check_armstrong(j):
             l.append(j)
             lim-=1
          j+=1
        
    return l


if __name__ == '__main__' :
# Print list of armstrong number in a range of 10000
  import time
  start_time = time.perf_counter()
  lim = abs(int(input('Enter range : ')))
  print(list_of_armstrong_num(lim))
  end_time = time.perf_counter()
  total_time = end_time - start_time
  print(f"It took about : {total_time:.2f}")

# Check whether the input number is armstrong or not
  num = abs(int(input('Enter a valid positive integer : ')))
  print(check_armstrong(num))
