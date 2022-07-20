def spiral_matrix(mat, rows, columns):
    top, left = 0, 0
    right = columns-1
    bottom = rows-1
    while left <= right and top <= bottom:
        for i in range(left, right+1):
            print(mat[top][i], end=" ")
        top += 1
        for i in range(top, bottom+1):
            print(mat[i][right], end=" ")
        right -= 1
        if top <= bottom:
            for i in range(right, left-1, -1):
                print(mat[bottom][i], end=" ")
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                print(mat[i][left], end=" ")
            left += 1


spiral_matrix([[10, 20, 30, 40],
              [15, 25, 35, 45],
              [27, 29, 37, 48]], 3, 4)
