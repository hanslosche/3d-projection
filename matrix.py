def matrix_multiplication(a, b):
    rows_a = len(a)
    rows_b = len(b)

    columns_a = len(a[0])
    columns_b = len(b[0])

    result_matrix = [[j for j in range(columns_b)] for i in range(rows_a)]
    if columns_a == rows_b:
        for x in range(rows_a):
            for y in range(columns_b):
                sum = 0
                for k in range(columns_a):
                    sum += a[x][k] * b[k][y]
                result_matrix[x][y] = sum
        return result_matrix
    else:
        print("Error! The Columns of the first Matrix must be equel to the row of the second Matrix ")
        return None
