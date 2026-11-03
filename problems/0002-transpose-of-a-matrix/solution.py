def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    if not a:
        return[]
    if any(len(row) != len(a[0]) for row in a):
        return -1
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]