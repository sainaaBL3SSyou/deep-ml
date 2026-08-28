def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	for l1 in range(len(matrix)):
		for l2 in range(len(matrix[l1])):
			matrix[l1][l2] = scalar * matrix[l1][l2]
	return matrix