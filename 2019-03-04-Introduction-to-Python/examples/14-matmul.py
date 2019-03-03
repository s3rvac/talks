# @ is for matrix multiplication since Python 3.5 (__matmul__).
#
# Requires numpy (http://www.numpy.org/).

import numpy as np

A = np.matrix('4 1; 9 3')
B = np.matrix('5 1; 3 8')

# Prints
#
#   [[23 12]
#    [54 33]]
#
print(A @ B)
