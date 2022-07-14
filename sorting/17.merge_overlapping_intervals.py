# def merge_intervals(intervals):
#     intervals.sort()
#     res = []
#     res.append(intervals[0])
#     for i in intervals:
#         if res[-1][0] <= i[0] <= res[-1][-1]:
#             res[-1][-1] = max(res[-1][-1], i[1])
#         else:
#             res.append(i)
#     print(res)


def merge_intervals(intervals):
    intervals.sort()
    res = 0
    for i in range(1, len(intervals)):
        if intervals[res][0] <= intervals[i][0] <= intervals[res][1]:
            intervals[res][1] = max(intervals[res][1], intervals[i][1])
        else:
            res += 1
            intervals[res] = intervals[i]
    print(intervals[:res+1])


merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
