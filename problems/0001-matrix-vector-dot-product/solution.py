def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0])!= len(b):
		return -1
	
	results = []
	for row in a:
		row_sum = sum(row[i] * b[i] for i in range(len(b)))
		results.append(row_sum)
	return results