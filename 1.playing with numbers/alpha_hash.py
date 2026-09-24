def hash():
    hashed = [0]*26
    return hashed


def check_freq_alpha(st):
    hash_list = hash()
    for char in st:
        asci = ord(char)
        hash_list[asci-97]+=1
    return hash_list

hash_list = check_freq_alpha('fsghnofihdniopwejfposjposdfwerjdodfihdfngoeiw')
q = ['a','d','f','e','z','s'] # we need to check their frequency in above string 
for char in q :
    asci = ord(char)
    print(hash_list[asci-97]) # to get the range in between 0 to 26

    
for i in q:
    nums = ord(i) - 97  
    print(i,":",hash_list[nums]) 
# print(hash_list,len(hash_list))       