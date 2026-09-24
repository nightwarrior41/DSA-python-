def partition(nums,low,high):
    i,j = low,high
    pi = nums[low]
    while i < j:
        while nums[i] <= pi and i <= high-1:
            i+=1
        while nums[j] >= pi and j >= low+1:
            j-=1
        if i < j:
           nums[i],nums[j] = nums[j],nums[i]
    
    nums[low],nums[j] = nums[j],nums[low]
    return j

def quicksort(nums,low,high):
    if low <high :
        pi = partition(nums,low,high)
        quicksort(nums,low,pi-1)
        quicksort(nums,pi+1,high)

l = [4,2,2,45,2,2324,43,547,2,45,13,344,1,23]
quicksort(l,0,len(l)-1)
print(l)
            