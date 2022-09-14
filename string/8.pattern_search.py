def lps_array(pattern):
    lps_array=[0]
    prefix_pointer=0
    suffix_pointer=1
    while suffix_pointer<len(pattern):
        if pattern[suffix_pointer]==pattern[prefix_pointer]:
            lps_array.append(prefix_pointer+1)
            prefix_pointer+=1
            suffix_pointer+=1
        else:
            if prefix_pointer==0:
                lps_array.append(0)
                suffix_pointer+=1
            else:
                prefix_pointer=lps_array[prefix_pointer-1]
    return lps_array


def pattern_search(str,pattern):
    pattern_lps=lps_array(pattern)
    # print(pattern_lps)
    str_pointer=0
    pat_pointer=0
    while str_pointer<len(str):
        if str[str_pointer]==pattern[pat_pointer]:
            str_pointer+=1
            pat_pointer+=1
        if pat_pointer==len(pattern):
            print(str_pointer-pat_pointer)
            pat_pointer=pattern_lps[pat_pointer-1]
        elif str_pointer<len(str) and pattern[pat_pointer]!=str[str_pointer]:
            if pat_pointer==0:
                str_pointer+=1
            else:
                pat_pointer=pattern_lps[pat_pointer-1]

pattern_search('ababcababaad','ababa')
