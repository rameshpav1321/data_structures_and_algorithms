def snake_matrix(mat):
    for i in range(len(mat)):
        if i % 2 == 0:
            for j in range(len(mat[i])):
                print(mat[i][j], end=" ")
        else:
            for j in range(len(mat[i])-1, -1, -1):
                print(mat[i][j], end=" ")


snake_matrix([[10, 20, 30, 40],
              [15, 25, 35, 45],
              [27, 29, 37, 48],
              [32, 33, 39, 50]])
