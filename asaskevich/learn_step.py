import numpy as np
from adapt_fix import adapt_fix
from get_block import get_block
from process_block import process_block


def learn_step(A, n, m, hor_blocks, ver_blocks, W, W_, step):
    E = 0
    for i in range(0, hor_blocks):
        for j in range(0, ver_blocks):
            block = get_block(i, j, n, m, A)
            X0_R, X0_G, X0_B = process_block(block)
            X = np.concatenate((X0_R, X0_G, X0_B))
            X = X.reshape(1, X.size)

            W, W_, e = adapt_fix(X, W, W_, step)
            # W, W_, E_G = adapt_fix(X0_G, W, W_, step)
            # W, W_, E_G = adapt_fix(X0_G, W, W_, step)
            # W, W_, E_B = adapt_fix(X0_B, W, W_, step)

            E += e

    return W, W_, E