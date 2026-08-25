def mean_calc(ls):
    a = 0
    for i in ls:
        a += i 
    return a/len(ls)
    
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []

    if mode == 'column':
        for col in range(len(matrix[0])):
            ls = []

            for row in range(len(matrix)):
                ls.append(matrix[row][col])

            means.append(mean_calc(ls))

    if mode == 'row':
        for row in range(len(matrix)):
            ls = []

            for col in range(len(matrix[row])):
                ls.append(matrix[row][col])

            means.append(mean_calc(ls))

    return means