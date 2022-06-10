import struct


def parse_value(data, offset, type):
    return struct.unpack(
        f'<{type}', data[offset: offset + struct.calcsize(type)]
    )[0]


def parse_array(data, offset, length, type):
    return list(struct.unpack(
        f'<{length}{type}',
        data[offset: offset + length * struct.calcsize(type)]
    ))


def parse_d(data, offset):
    result = dict()
    f1_size, f1_addr = struct.unpack('<HH', data[offset: offset + 4])
    f1_arr = parse_array(data, f1_addr, f1_size, 'f')
    result['D1'] = f1_arr
    f2_size, f2_addr = struct.unpack('<HI', data[offset + 4: offset + 10])
    f2_arr = parse_array(data, f2_addr, f2_size, 'h')
    result['D2'] = f2_arr
    f3_size, f3_addr = struct.unpack('<HI', data[offset + 10: offset + 16])
    f3_arr = parse_array(data, f3_addr, f3_size, 'f')
    result['D3'] = f3_arr
    result['D4'] = parse_value(data, offset + 16, 'B')
    result['D5'] = parse_value(data, offset + 17, 'Q')
    return result


def parse_c(data, offset):
    result = dict()
    result['C1'] = parse_value(data, offset, 'I')
    f2_addr = parse_value(data, offset + 4, 'H')
    result['C2'] = parse_d(data, f2_addr)
    f3_size, f3_addr = struct.unpack('<II', data[offset + 6: offset + 14])
    f3_arr = parse_array(data, f3_addr, f3_size, 'H')
    result['C3'] = f3_arr
    result['C4'] = parse_value(data, offset + 14, 'Q')
    return result


def parse_b(data, offset):
    result = dict()
    result['B1'] = parse_value(data, offset, 'H')
    result['B2'] = parse_value(data, offset + 2, 'I')
    result['B3'] = parse_value(data, offset + 6, 'b')
    return result


def parse_a(data, offset):
    result = dict()
    result['A1'] = parse_value(data, offset, 'I')
    result['A2'] = parse_value(data, offset + 4, 'i')
    result['A3'] = parse_value(data, offset + 8, 'h')
    result['A4'] = parse_value(data, offset + 10, 'b')
    result['A5'] = parse_value(data, offset + 11, 'f')
    f6_addr = parse_value(data, offset + 15, 'H')
    result['A6'] = parse_b(data, f6_addr)
    f7_size, f7_addr = struct.unpack('<IH', data[offset + 17: offset + 23])
    f7 = list()
    for i in range(f7_size):
        f7.append(parse_c(data, f7_addr + i * 22))
    result['A7'] = f7
    return result


def main(data):
    return parse_a(data, 4)


print(main(
    b'fDMM<k\rX:Y,\xf7\xb7B\xfa_@\xbd>\x1b\x00\x02\x00\x00\x00\x96\x00H'
    b'\\\xec\x12\xe7\xe3\xcf\xd1\xd2\x11\xbe&!1?\x8e\x9fj\xbf\xb8\xed\x03E\xe9\x19'
    b'\n\x19\xa2\xbe\x0cD\x1a\xbf+\xd6m?DyL?\x03\x00"\x00\x03\x00.\x00'
    b'\x00\x00\x04\x004\x00\x00\x00b\x19q\x8e\x1e!\xde\xc61\x11C.x\xa5\x92\x13'
    b'?\xd9ma\xbf\x94\xcft?\x8b;\xacrTmP\xbf\xe1\x07d=\x03\x00a\x00\x02\x00m'
    b'\x00\x00\x00\x02\x00q\x00\x00\x00\xdb\x1a48;\xca\x0e\\\xaeC~\xb2\x1b\x80;'
    b'^\xefD\x00\x02\x00\x00\x00]\x00\x00\x00#\x9f\xf1\xd7>\x94\t\xa0\x8455\xe6'
    b'y\x00\x02\x00\x00\x00\x92\x00\x00\x00R\x10\x8cu\xfe6oA'
))
