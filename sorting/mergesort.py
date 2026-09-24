# Merging two sorted subarray
def merge(l,r):
    n,m = len(l),len(r)
    i,j=0,0
    result = []
    while i <n and j < m:
        if l[i] <= r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1   
    #copying left out elements from anyone one of two subarrays
    if i < n:
        while i< n:
            result.append(l[i])
            i+=1
    if j < m:
        while j < m:
            result.append(r[j])
            j+=1
    return result

# Dividiong a array into two subarrays

def merge_sort(arr):
    if len(arr) <= 1:
           return arr
    mid = len(arr)//2
    left_sub = merge_sort(arr[:mid])
    right_sub = merge_sort(arr[mid:])
    return merge(left_sub,right_sub)


print(merge_sort([3,2,5,12,3,346,1,23,5,4,15,3,3]))