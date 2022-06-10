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
    result['D1'] = parse_value(data, offset, 'q')
    f2_size, f2_addr = struct.unpack('<II', data[offset + 8: offset + 16])
    f2_arr = parse_array(data, f2_addr, f2_size, 'I')
    result['D2'] = f2_arr
    return result


def parse_c(data, offset):
    result = dict()
    result['C1'] = parse_d(data, offset)
    result['C2'] = parse_value(data, offset + 16, 'f')
    result['C3'] = parse_value(data, offset + 20, 'H')
    result['C4'] = parse_value(data, offset + 22, 'q')
    result['C5'] = parse_value(data, offset + 30, 'b')
    f6_size, f6_addr = struct.unpack('<HI', data[offset + 31: offset + 37])
    f6_arr = parse_array(data, f6_addr, f6_size, 'd')
    result['C6'] = f6_arr
    return result


def parse_b(data, offset):
    result = dict()
    result['B1'] = parse_value(data, offset, 'B')
    result['B2'] = parse_value(data, offset + 1, 'I')
    return result


def parse_a(data, offset):
    result = dict()
    result['A1'] = parse_value(data, offset, 'f')
    f2_size, f2_addr = struct.unpack('<HI', data[offset + 4: offset + 10])
    f2_arr = ''.join(
        map(bytes.decode, parse_array(data, f2_addr, f2_size, 'c'))
    )
    result['A2'] = f2_arr
    result['A3'] = parse_value(data, offset + 10, 'd')
    result['A4'] = parse_value(data, offset + 18, 'Q')
    result['A5'] = parse_value(data, offset + 26, 'h')
    f7_size, f7_addr = struct.unpack('<HH', data[offset + 28: offset + 32])
    f7_arr = parse_array(data, f7_addr, f7_size, 'I')
    f7 = list()
    for addr in f7_arr:
        f7.append(parse_b(data, addr))
    result['A6'] = f7
    result['A7'] = parse_c(data, offset + 32)
    return result


def main(data):
    return parse_a(data, 4)


print(main(
    b'\x1aQTCu\x08b\xbf\x05\x00I\x00\x00\x00\x96\x94\x08\x9d\x92R\xec\xbf\x1ec'
    b'/Q\x0cZ\xf18\xd2\xa2\x04\x00b\x00\x89\xa1OAF\x06\xcb\xca\x07\x00\x00\x00'
    b'r\x00\x00\x00\xc9\x83\x08?\x80s\xc2\x9cjZ_4\xdc\xa6z\x03\x00\x8e\x00\x00'
    b'\x00hptue\xbbhVj\xc7o\xd6\xf3\xc4a8\x01\xeb]\xb6sj\xea\xe5\xe5N\x00'
    b'\x00\x00S\x00\x00\x00X\x00\x00\x00]\x00\x00\x00\x1e\x95\xd7\xf6\xf2\x87'
    b'3\x1e\x1b\x8f\x87\xdc\xb2\xa39\x8a}\x00\xdc\xdfz\xbdq<\xb4\x8b1\xa4\x1cw'
    b'8n\x99\xee\xdb\xbf\xf0\x1e\x06T\x8a_\xba\xbf\x08\xdbn}]\xc8\xd6?'
))
