def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    ls = []
    try:
        for i in range(len(a)):
            c = 0
            for y in range(len(b)):
                c += a[i][y] * b[y]
            ls.append(c)

        return ls
    except IndexError:
        return -1