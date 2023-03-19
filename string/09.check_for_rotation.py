def check_rotation(str1,str2):
    # temp=''
    # str_len=len(str1)
    # for i in range(str_len):
    #     temp=str1[1:]+str1[0]
    #     if temp==str2:
    #         return True
    #     else:
    #         str1=temp
    # return False
    if len(str1)!=len(str2):
        return False
    else:
        temp=str1+str1
        if temp.find(str2)>=0:
            return True
        else:
            return False

print(check_rotation('abab','abba'))
