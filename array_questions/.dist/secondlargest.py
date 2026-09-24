# find the second largest element in the array
def second_largest(nums):
    if len(nums) <= 1:
        return -1
    first = float('-inf')
    second = float('-inf')
    flag = False
    for i in range(len(nums)-1):
        if nums[i] > first:
            second = first 
            first = nums[i]
        elif nums[i] > second and nums[i] != first:
            second = nums[i]
            flag = True
    # just in case all element are same then it will return -inf so instead I do this to stop it
    if flag:
       return second
    else:
        return -1
       

l = [5,5,5,5,5,5]
print(second_largest(l))