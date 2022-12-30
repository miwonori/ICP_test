# This is a sample Python script._

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import time
import icp

N = 10
num_tests = 100
dim = 3
noise_sigma = 0.01
translation = 0.1
rotation = 0.1

def rotation_matrix(axis, theta):
    axis = axis/np.sqrt(np.dot(axis, axis))
    a = np.cos(thetat/2.0)
    b, c, d = -axis*np.sin(theta/2.0)

    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                  [2*(b*c+a*d), a*a+c*c-b*b-d*d, 2*(c*d-a*b)],
                  [2*(b*d-a*c), 2*(c*d+a*b), a*a+d*d-b*b-c*c]])


def test_best_fit():
    # Generate a random dataset

    A = np.random.rand(N, dim)
    total_time = 0

    for i in range(num_tests):
        B = np.copy(A)

        # translate
        t = np.ramdom.rand(dim)*translation




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
