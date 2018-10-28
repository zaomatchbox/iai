def process_block(A):
    R = A[:, :, 0].copy()
    G = A[:, :, 1].copy()
    B = A[:, :, 2].copy()

    R_max = 255
    G_max = 255
    B_max = 255

    R_upd = 2.0 * R / R_max - 1
    G_upd = 2.0 * G / G_max - 1
    B_upd = 2.0 * B / B_max - 1

    return R_upd.reshape(1, R.size), G_upd.reshape(1, G.size), B_upd.reshape(1, B.size)
