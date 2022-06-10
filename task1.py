from math import acos, cos, log, sqrt


def main(y, z, x):
    return (
        sqrt(
            (pow(sqrt(44*x*x-pow(y, 3)-z), 5)-22*pow(abs(y), 4))
            / (pow(acos(x), 2)-37*pow((8*y*y+50*z+pow(x, 3)), 5))
        )
        + (
            (pow(x, 7)+pow(z*z-1-pow(y, 3), 2)/16)
            / (pow(cos(y), 5)-83*pow(log(1+x+56*z*z, 2), 3))
        )
    )


print(main(0.85, -0.26, -0.99))
