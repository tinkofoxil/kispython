def main(x):
    a = format(x, '032b')
    a = a[2] + a[0:2] + a[20:32] + a[3:7] + a[7:20]
    a = int(hex(int(a, 2)), 0)
    return a


print(main(0x4055eef4))
