# def transpose_matrix(mat, rows, columns):
#     for i in range(rows):
#         for j in range(columns):
#             print(mat[j][i], end=" ")
#         print()
# def transpose_matrix(mat, rows, columns):
#     for i in range(rows):
#         for j in range(i+1, columns):
#             mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
#     print(mat)

def transpose_matrix(mat, rows, columns):
    # res = [[0]*rows for _ in range(columns)]
    # for i in range(rows):
    #     for j in range(columns):
    #         res[j][i] = mat[i][j]
    print(list(map(list, zip(*mat))))


transpose_matrix([[1, 2, 3],
                  [4, 5, 6]], 2, 3)
