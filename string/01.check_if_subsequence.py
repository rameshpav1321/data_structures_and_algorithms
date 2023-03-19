def chk_sub_sequence(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    i = 0
    j = 0
    while(i <= str1_len and j <= str2_len):
        if j == str2_len:
            return True
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            i += 1
    return False
