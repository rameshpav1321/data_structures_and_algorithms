def function(lst):
    res=1
    count=1
    for i in range(1,len(lst)):
      if (lst[i]%2==0 and lst[i-1]%2!=0) or (lst[i]%2!=0 and lst[i-1]%2==0):
        count+=1
        res=max(res,count)
      else:
        count=1
    return res




print(function([5, 10, 20, 6, 3, 8]))
