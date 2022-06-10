from math import ceil


def main(y, z, x):
    res = 0
    for i in range(1, 8):
        res += pow(53*pow(x[ceil(i/4)-1], 2)-93*pow(z[7-i], 3)-29*y[i-1], 6)
    return res


print(main(
    [0.77, -0.25, -0.13, 0.28, 0.62, 0.12, 0.55],
    [-0.44, -0.37, 0.45, 0.71, 0.35, 0.03, 0.24],
    [0.18, -0.37, 0.07, 0.5, -0.65, -0.99, 0.74]
))
