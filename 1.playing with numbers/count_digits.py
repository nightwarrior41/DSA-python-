def log_count_digit(num):
    import math as m
    if num == 0 :
        return 1
    else:
        return int(m.log10(abs(num))+1)
    
def conventional_count_digit(num):
    n = abs(num) ; count = 0
    while n > 0 :
        count+=1
        n = n//10
    return count

# if __name__ == '__main__':
#   num = int(input("Enter your number : "))
#   print(f'logarithmic way : {log_count_digit(num)}')
#   print(f'Conventional way : {conventional_count_digit(num)}')
  
  
