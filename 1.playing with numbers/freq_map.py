# A small use case of dictionary

def frequency_of_num(l):
    dict = {}
    for i in range(len(l)):
        if l[i] in dict:
            dict[l[i]] += 1
        else:
            dict[l[i]] = 1
            
    return dict

# The pythonic way 
def frequency_of_num_new(l):
    dict = {};n=len(l)
    for i in range(n):
        dict[l[i]] = dict.get(l[i],0) + 1
    return dict

if __name__=='__main__':
    print(frequency_of_num_new([11,11,1,2,3,3,2,2,4]))