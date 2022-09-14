def function(lst):
    min_ele=lst[0]
    max_sum=lst[1]-lst[0]
    for i in range(1,len(lst)):
      min_ele=min(min_ele,lst[i-1])
      max_sum=max(max_sum,lst[i]-min_ele)
    if max_sum>=0:
      return max_sum
    else:
      return -1



print(function([30,10,8,2]))
