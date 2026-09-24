def selectionsort(nums):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[min_index] > nums[j]: # if you use '<' instead of '>' you get sorted array descending order else in ascending order
                min_index = j
        nums[min_index],nums[i] = nums[i],nums[min_index] # swap the smallest number with current starting index
    return nums


print(selectionsort([2,1,54,4,23,8]))
        