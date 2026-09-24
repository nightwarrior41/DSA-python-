def bubblesort(nums):
    for i in range(len(nums)-1):
        swapped = False # condition for sorted array
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                swapped =True
                nums[j],nums[j+1] = nums[j+1],nums[j]
        if not swapped:
            # return nums
            break
    # return nums

l = [2,1,3,5,6,7,3,5]
bubblesort(l) # if you do print(bubblesort(l)) then output will be none because we removed the return statement here since there inplace operation is occuring
print(l)