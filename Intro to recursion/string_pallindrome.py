# The first thought
def check_str_pallindrome(s):
    rev = ''
    for i in range(len(s)-1,-1,-1):
        rev += s[i]
    return rev == s

# Iterative way and the two pointer approach
def check_str_pallindrome_i(s):
    l = 0 ; r = len(s)-1
    while l <= r :
        if s[l] == s[r]:
            l+=1;r-=1
        else:
            return False
    return True

# Recursive way and the two pointer approach
def check_str_pallindrome_r(l,r,s):
    if l <= r:
        if s[l] == s[r] :
            l+=1 ; r-=1
            return check_str_pallindrome_r(l,r,s)
        else:
            return False
    else:
        return True
print(check_str_pallindrome_r(0,4,'nitin'))

def reverseString(s):
        ls = list(s)
        l = 0 ; r = len(ls)-1
        while l <= r:
            ls[l],ls[r] = ls[r],ls[l]
            l+=1 ; r-=1
        return ls

print(reverseString('hello'))
        