def s10_to_sys(a, b):
    c = []
    while a != 0:
        c.append(str(a % b))
        a //= b
    return c[::-1]
def sys_to_s10(a, b):
    return int(str(a), b)