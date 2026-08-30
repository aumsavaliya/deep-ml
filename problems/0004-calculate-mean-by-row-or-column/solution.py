def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	if mode == 'row' :
		groups = matrix
	elif mode == 'column':
		groups = zip(*matrix)

		
	return [sum(g)/len(g) for g in groups]