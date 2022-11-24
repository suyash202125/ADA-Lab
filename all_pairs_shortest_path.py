from cmath import inf

def FW(matrix):

    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][k] == inf or matrix[k][j] == inf:
                    continue
                else:
                    cost = matrix[i][k] + matrix[k][j]
                    matrix[i][j] = min(matrix[i][j], cost)
    return matrix


input_matrix =  [[0, 5, 2, inf],
                [inf, 0, 4, 3],
                [3, inf, 0, 3],
                [inf, inf, inf, 0]]

for row in FW(input_matrix):
    print(row)