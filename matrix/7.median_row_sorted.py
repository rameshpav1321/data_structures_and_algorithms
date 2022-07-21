from bisect import bisect_right


def median_row_sorted(mat, rows, columns):
    min_ele = mat[0][0]
    max_ele = mat[0][columns-1]
    for i in range(1, rows):
        if mat[i][0] < min_ele:
            min_ele = mat[i][0]
        if mat[i][columns-1] > max_ele:
            max_ele = mat[i][columns-1]
    median_pos = (rows*columns+1)//2
    while min_ele < max_ele:
        mid = (min_ele+max_ele)//2
        mid_pos = 0
        for i in range(rows):
            mid_pos += bisect_right(mat[i], mid)
        if mid_pos < median_pos:
            min_ele = mid+1
        else:
            max_ele = mid
    print("Median of the given matrix is: ", min_ele)


median_row_sorted([[5, 10, 20, 30, 40], [1, 2, 3, 4, 6],
                  [11, 13, 15, 17, 19]], 3, 5)
