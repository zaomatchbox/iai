def get_n_m(w, h, L):
    for n in range(1, w):
        for m in range(1, h):
            if w % n == 0:
                if h % m == 0:
                    if n * m == L:
                        return n, m