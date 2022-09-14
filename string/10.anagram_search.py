def anagram_search(str,pattern):
    str_arr=[0*256]
    patt_arr=[0*256]
    for i in range(len(pattern)):
        str_arr[str[i]]+=1
        patt_arr[pattern[i]]+=1
    
    for i in range(len(pattern),len(str)):
        if str_arr==patt_arr:
            return True
        else:
            str_arr[str[i]]+=1
            str_arr[str[i-len(pattern)]]-=1
    return False