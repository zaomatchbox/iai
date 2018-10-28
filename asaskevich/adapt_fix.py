def adapt_fix(X, W, W_, step):
    # W, W_ = normalize(W), normalize(W_)
    Y = X * W
    X_ = Y * W_
    dX = X_ - X

    # s1 = 1.0 / (Y * Y)
    # s2 = 1.0 / (X * X)
    #
    W_t = W_ - step * Y * dX
    Wt = W - step * X * dX * W_
    # W_t = W_ - s1 * Y * dX
    # Wt = W - s2 * s2 * X * dX * W_

    E = sum(sum(dX * dX))

    return Wt, W_t, E
