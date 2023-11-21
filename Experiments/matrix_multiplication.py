mat_one = [[1,2,3],[4,5,6],[7,8,9]]
mat_two = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]


def assert_lists_same_length(matrix_one, matrix_two):
    matrix_one_length = len(matrix_one[0])
    if not all(len(l) == matrix_one_length for l in matrix_one):
        raise ValueError('not all rows in matrix one are the same length!')
    matrix_two_length = len(matrix_two[0])
    if not all(len(l) == matrix_two_length for l in matrix_two):
        raise ValueError('not all rows in matrix two are the same length!')


def matrix_report(matrix_one, matrix_two):
    mat_one_rows = len(matrix_one)
    mat_one_cols = len(matrix_one[0])
    mat_two_rows = len(matrix_two)
    mat_two_cols = len(matrix_two[0])
    print("matrix one has the shape: {0} by {1}".format(mat_one_rows, mat_one_cols))
    print("matrix two has the shape: {0} by {1}".format(mat_two_rows, mat_two_cols))

def matrix_multiplication(matrix_one, matrix_two):
    mat_one_rows = len(matrix_one)
    mat_one_cols = len(matrix_one[0])
    mat_two_rows = len(matrix_two)
    mat_two_cols = len(matrix_two[0])

    # Check if multiplication is possible
    if mat_one_cols != mat_two_rows:
        raise ValueError("Number of columns in matrix one must be equal to number of rows in matrix two")

    # Initialize result matrix with zeros
    result = [[0 for _ in range(mat_two_cols)] for _ in range(mat_one_rows)]

    # Perform matrix multiplication
    for i in range(mat_one_rows):
        for j in range(mat_two_cols):
            for k in range(mat_two_rows):
                result[i][j] += matrix_one[i][k] * matrix_two[k][j]

    return result
                

assertion = assert_lists_same_length(mat_one,mat_two)
matrix_report(mat_one, mat_two)
matmul_result = matrix_multiplication(mat_one, mat_two)
print(matmul_result)