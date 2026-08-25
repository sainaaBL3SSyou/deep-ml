def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    lst = []
    # print(ls)
    for col in range(len(a[0])):
        ls = [0] * len(a)
        # print(ls)
        for row in range(len(a)):
            # print(a[row][col])
            ls[row] = a[row][col]
        lst.append(ls)
        
    return lst
        
            