# The most common way
# a = [1,2,3,4,5,6,7]
# print(a[::-1])

# reverse array using recursion
# def reverse_array(arr,l):
#     if l == 0:
#         return arr
#     arr.append(arr[l])
#     return reverse_array(arr,l-1)

# print(reverse_array([1,2,3,4,5,6],5))

# The inplace reverse method of list, num.reverse() reverse the list in place and it retrun none
# num = [1,2,3,4]
# num.reverse()
# print(num)


# Swap the number
def swapr(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b

# Reverse an array recursion
def reverse_array(l,r,arr):
    if l >= r:
        return arr
    arr[l],arr[r] = swapr(arr[l],arr[r]) # python way of swapping (a,b) = (b,a)
    return reverse_array(l+1,r-1,arr)

#  Using loop reversing an array
def reverse_array_optimized(l,r,arr):
    while l <= r:
        arr[l],arr[r] = swapr(arr[l],arr[r])
        l+=1 ; r-=1
    return arr

l=[1,2,3,4,5,6]
# print(reverse_array(1,len(l)-3,l))
print(reverse_array_optimized(0,len(l)-1,l))

