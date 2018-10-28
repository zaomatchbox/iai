from PIL import Image
import numpy as np
import scipy.misc as smp
import matplotlib.pyplot as plt
from pylab import *

from get_init_weights import get_init_weights
from get_n_m import get_n_m
from get_z import get_Z
from learn import learn
from restore_pic import restore_pic


def run(L=12, p=20, step=0.01, e=2, fname='image.jpg'):
    im = Image.open(fname)
    pixels_matrix = np.asarray(im)
    w = pixels_matrix.shape[0]
    h = pixels_matrix.shape[1]
    # L = 12
    # p = 20
    # step = 0.01
    # e = 10
    N = h * w
    block_size = N / L
    hor_blocks, ver_blocks = get_n_m(w, h, L)
    n, m = w / hor_blocks, h / ver_blocks
    Z = get_Z(block_size, L, p)

    if Z > 1:
        print ('Error: Z > 1')
        return 0, 0, 0

    if 0.1 * p < e:
        print ('Error: e > 0.1 * p')
        return (0, 0, 0)

    W, W_ = get_init_weights(p, block_size * 3)
    W, W_, E, iteration, errs = learn(pixels_matrix, n, m, hor_blocks, ver_blocks, W, W_, step, e)

    P = restore_pic(pixels_matrix, n, m, hor_blocks, ver_blocks, W, W_)
    img = smp.toimage(P)
    img.show()

    plt.plot(errs)
    plt.xlabel("epochs")
    plt.ylabel("E")
    plt.show()
    print ('iterations = %s, err = %s, for input L = %s, e = %s, step = %s, p = %s, Z=%s' % (
        iteration, E, L, e, step, p, Z))

    return (iteration, E, errs)


# x = []
# y = []
#
# files = ['dog1.jpg', 'dog2.jpg', 'dog3.jpg', 'dog4.jpg', 'dog5.jpg', 'dog6.jpg', 'dog7.jpg']
#
# for f in files:
#     i, e, _ = run(L=12, p=20, e=2, fname=f)
#     x.append(f)
#     y.append(i)
#
# plt.plot(x, y)
# plt.xlabel("file")
# plt.ylabel("iterations")
# plt.show()

run(L=6, p=15, e=1, fname='test.jpg')
#
