def get_block(i, j, n, m, A):
    left = (i * n)
    right = (i + 1) * n
    top = (j * m)
    bottom = (j + 1) * m
    return A[left:right, top:bottom]