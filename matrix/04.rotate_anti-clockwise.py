# def rotate_matrix(mat, rows, columns):
#     for i in range(columns-1, -1, -1):
#         for j in range(rows):
#             print(mat[j][i], end=" ")
#         print()
def rotate_matrix(mat):
    mat = list(map(list, zip(*mat)))
    i = 0
    rows = len(mat)
    columns = len(mat[0])
    while i < columns:
        for j in range(rows//2):
            mat[j][i], mat[rows-1-j][i] = mat[rows-1-j][i], mat[j][i]
        i += 1
    print(mat)


rotate_matrix([[10, 20, 30, 40],
               [15, 25, 35, 45],
               [27, 29, 37, 48]])
