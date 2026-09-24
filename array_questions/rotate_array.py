# Rotate array by one place 
def rotate_by_one(l):
    j = l[-1]
    for i in range(len(l)-2 ,-1,-1):
        l[i+1] = l[i]
    l[0] = j
    
     
l = [1,2,3,4,5]
rotate_by_one(l)
print(l)

# rotate array by k place 
# first naive approach : rotate by one k times
def rotate_by_k_naive(l,k):
    for i in range(k%len(l)): 
        j = l[-1]
        for i in range(len(l)-2 ,-1,-1):
            l[i+1] = l[i]
        l[0] = j
        
        
# optimal approach inplace too 
# right reverse
def rotate_by_k(l,k):
    l.reverse()
    l[:k%len(l)] = reversed(l[:k%len(l)])
    l[k%len(l):] = reversed(l[k%len(l):])
    

l = [1,2,3,4,5]

rotate_by_k(l,5)
print(l)
    

    
