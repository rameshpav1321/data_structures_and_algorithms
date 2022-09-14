# def longest_substring(str):
#     my_set={str[0]}
#     count=1
#     curr_count=1
#     for i in range(1,len(str)):
#         if str[i]!=str[i-1] and str[i] not in my_set:
#             curr_count+=1
#             count=max(count,curr_count)
#             my_set.add(str[i])
#         else:
#             curr_count=1
#             my_set.clear()
#             my_set.add(str[i])
#     return count
def lengthOfLongestSubstring(str):
        if str=="":
            return 0
        my_dict={}
        count=0
        curr_count=0
        for i in range(len(str)):
            if str[i] not in my_dict:
                my_dict[str[i]]=i
                # curr_count+=1
                curr_count=len(my_dict)
                print("print1",curr_count)
                count=max(count,curr_count)
            else:
                curr_count=i-my_dict[str[i]]
                print("print2",curr_count)
                # del my_dict[str[i]]
                # my_dict.clear()
                my_dict[str[i]]=i
                count=max(count,curr_count)
                # else:
                #     my_dict.clear()
                #     my_dict[str[i]]=1
                #     count=max(count,len(my_dict))
        print(count)

lengthOfLongestSubstring("pwwkew")
lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("dvdf")
lengthOfLongestSubstring("abba")

