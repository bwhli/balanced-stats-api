def format_number(hex):
    return int(hex, 16)  # noqa F523


def hex_to_int(hex, dec):
    num = int(hex, 16) / 10 ** dec
    if num - int(num) == 0:  # If num is a whole number.
        return int(num)
    else:
        return num
