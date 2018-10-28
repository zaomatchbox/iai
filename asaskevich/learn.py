from learn_step import learn_step


def learn(A, n, m, hor_blocks, ver_blocks, W, W_, step, e):
    iteration = 0
    E = 10e100
    errs = []
    while E > e:
        W, W_, E = learn_step(A, n, m, hor_blocks, ver_blocks, W, W_, step)
        iteration += 1

        if E < 1000:
            errs.append(E)

        if iteration % 100 == 0:
            print (E)
        #
        # if iteration > 15:
        #     break


    return W, W_, E, iteration, errs
