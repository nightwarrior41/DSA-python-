def move_to_last(l):
    i , j = 0 , len(l)-1
    while i < j:
        if l[i] == 0 :
            while l[j] == 0:
                if j == 0:
                    return l
                j-=1
            l[i],l[j] = l[j],l[i]
            j-=1
        i+=1
    return l
   
l = [1,0,2,4,3,0,0,3,5,1]
l=move_to_last(l)
print(l)


# Brute force
def moveZeroes(nums):
        j = []
        for i in range(len(nums)):
            if nums[i] != 0 :
                j.append(nums[i])
        z = len(nums) - len(j)
        nums = j+z*[0]
        return nums
        
l = [1,2,0,3,0,4,0,1]
print(moveZeroes(l))

