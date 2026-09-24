# Interview or conventional method
def reverse_num(num):
    n = num
    rev = 0
    while n > 0 :
        rev = rev*10 + (n%10)
        n = n//10
    return rev

def check_pallindrome(num):
    return reverse_num(num) == num
    

if __name__=='__main__':   
# Input the number 
  num = abs(int(input('Enter the number : '))) # num should be positive
  print(f'{check_pallindrome(num)} the {num} is a pallindrome !!')
  
# Python way 
  n = str(num)
  n = n[::-1]
  print(int(n) == num)
