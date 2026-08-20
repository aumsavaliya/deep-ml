def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a) == 0:
		return -1
	
	
	nums_col = len(a[0])
	if nums_col != len(b):
		return -1
	result =[]
	for r in a :
		 total = sum((r[i]*b[i] for i in range(nums_col)))
		 result.append(total)
	return result