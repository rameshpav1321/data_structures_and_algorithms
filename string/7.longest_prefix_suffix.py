def longest_prefix_suffix(str):
    lps_array=[0]
    # lps_array[0]=0
    prefix_pointer=0
    suffix_pointer=1
    while suffix_pointer<len(str):
        if str[prefix_pointer]==str[suffix_pointer]:
            lps_array.append(prefix_pointer+1)
            prefix_pointer+=1
            suffix_pointer+=1
        else:
            if prefix_pointer==0:
                lps_array.append(0)
                suffix_pointer+=1
            else:
                prefix_pointer=lps_array[prefix_pointer-1]
    print(lps_array)

longest_prefix_suffix('aaabaaaac')