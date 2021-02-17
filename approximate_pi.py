import random
import math

def ratio_points_circle_method(num_points, verbose=0):
    in_circle = 0
    for i in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        dist = math.sqrt(x**2 + y**2)
        if verbose >= 1:
            print('approx_pi: [{}/{}] Generated point ({}, {}) with d={}'.format(i, num_points, x, y, dist))
        if dist <= 1:
            in_circle += 1
    return 4*(in_circle/num_points)

if __name__ == '__main__':
    i = 10
    while i <= 100000000:
        print(i, ratio_points_circle_method(i))
        i *= 10

