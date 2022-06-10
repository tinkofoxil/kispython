from math import sin, cos


def main(z):
    if z < 33:
        return pow(sin(62*z*z + pow(z, 3)/34), 7) + pow(z, 4)/48
    elif 33 <= z < 127:
        return pow(sin(z), 7)/17 - pow(z, 4)/39 - 43*pow(z, 6)
    elif 127 <= z < 213:
        return pow(pow(z, 3)/47 - z - 1, 2) + 58 + 15*pow((46*z*z*z+z*z/33), 3)
    elif z >= 213:
        return 48*pow(cos(65 + pow(z, 3) + z), 7) + 5*pow(z, 5)


print(main(28))
