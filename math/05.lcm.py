x = int(input())
y = int(input())
lcm_found = False
lcm = 0
max_res = max(x, y)
min_res = min(x, y)
while(not lcm_found):
    if(max_res % min_res == 0):
        lcm = max_res
        lcm_found = True
    else:
        max_res += max(x, y)
print(lcm)
