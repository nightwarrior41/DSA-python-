def insertionsort(nums):
    for i in range(1,len(nums)):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] =key
    
    
l = [1,2,4,6,1,4,6,2]
insertionsort(l)
print(l)
                    