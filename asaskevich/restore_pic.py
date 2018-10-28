import numpy as np
from get_block import get_block
from process_block import process_block


def restore_pic(A, n, m, hor_blocks, ver_blocks, W, W_):
    P = A.copy()
    for i in range(0, hor_blocks):
        for j in range(0, ver_blocks):
            block = get_block(i, j, n, m, A)
            X0_R, X0_G, X0_B = process_block(block)
            X0 = np.concatenate((X0_R, X0_G, X0_B))
            X0 = X0.reshape(1, X0.size)

            # X = X0 * W * W_
            X = X0 * W
            # X_R = X0_R * W * W_
            # X_G = X0_G * W * W_
            # X_B = X0_B * W * W_
            #
            # R = (255 * (X_R[0] + 1) / 2)
            # G = (255 * (X_G[0] + 1) / 2)
            # B = (255 * (X_B[0] + 1) / 2)

            X = (255 * (X[0] + 1) / 2)
            X = X.reshape(3, n * m)

            left = (i * n)
            right = (i + 1) * n
            top = (j * m)
            bottom = (j + 1) * m

            P[left:right, top:bottom, 0] = X[0].reshape(n, m)
            P[left:right, top:bottom, 1] = X[1].reshape(n, m)
            P[left:right, top:bottom, 2] = X[2].reshape(n, m)

    return P