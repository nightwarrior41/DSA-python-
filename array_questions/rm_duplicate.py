# Bruteforce
def rm_dup(l):
    dict = {}
    j = 0
    for i in l:
        dict[i] = 0
    for i in dict.keys():
        l[j] = i
        j+=1
    for i in range(j,len(l)):
        l[i] = 999
    return j

#The optimal solution
def rm_dup2(l):
    n = 0 
    if len(l)==1:
        return 1
    for i in range(1,len(l)):
        if l[n] != l[i]:
            n+=1
            l[n]=l[i]
            
    return n+1
            




l = [1,1,1,2,3,4,4,7,9,9,9,10]
unique_ele = rm_dup2(l)
print(l,unique_ele)
