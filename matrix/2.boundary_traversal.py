# def boundary_traversal(mat):
#     if len(mat) == 1 or len(mat[0]) == 1:
#         print(mat)
#     else:
#         for i in range(len(mat)):
#             if i == 0:
#                 for j in range(len(mat[i])):
#                     print(mat[i][j], end=" ")
#                 for j in range(len(mat[i])):
#                     if j == len(mat[i])-1:
#                         for k in range(1, len(mat)):
#                             print(mat[k][j], end=" ")

#             if i == len(mat)-1:
#                 for j in range(len(mat[i])-2, -1, -1):
#                     print(mat[i][j], end=" ")
#                 for j in range(len(mat[i])):
#                     if j == 0:
#                         for k in range(len(mat)-2, 0, -1):
#                             print(mat[k][j], end=" ")

def boundary_traversal(mat, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if i == 0:
                print(mat[i][j], end=" ")
            elif i == rows-1:
                print(mat[i][j], end=" ")
            elif j == 0:
                print(mat[i][j], end=" ")
            elif j == columns-1:
                print(mat[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()


boundary_traversal([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [1, 2, 3, 4],
                    [5, 6, 7, 8]], 4, 4)
