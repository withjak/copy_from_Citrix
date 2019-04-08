from collections import namedtuple


def mapping2():
    mapping = {}
    red = lambda r: r - 5
    green = lambda g: g - 5
    blue = lambda b: b - 5
    r = red(260)
    g = green(260)
    b = blue(260)
    print('Mapping of each character')
    for char in 'abcdefghijklmnopqrstuvwxyz ':
        print(char, r, 0, 0)
        mapping[char] = (r, 0, 0)
        r = red(r)
    for char in r"""`~!@#$%^&*()_+-={}|[]\:";'<>?,./""":
        print(char, 0, g, 0)
        mapping[char] = (0, g, 0)
        g = green(g)
    for char in """0123456789\n""":
        print(char, 0, 0, b)
        mapping[char] = (0, 0, b)
        b = blue(b)
    return mapping


def mapping():
    mapping = {}

    def color_shades(color=255):
        while color > 50:
            yield color
            color -= 5

    print('Mapping of each character')

    red = color_shades()
    for char in 'abcdefghijklmnopqrstuvwxyz ':
        r = next(red)
        print(char, r, 0, 0)
        mapping[char] = (r, 0, 0)

    green_shade = color_shades()
    for char in r"""`~!@#$%^&*()_+-={}|[]\:";'<>?,./""":
        g = next(green_shade)
        print(char, 0, g, 0)
        mapping[char] = (0, g, 0)

    blue_shade = color_shades()
    for char in """0123456789\n""":
        b = next(blue_shade)
        print(char, 0, 0, b)
        mapping[char] = (0, 0, b)

    return mapping


def rev_map():
    _mapping = mapping()
    rev_mapp = {}
    for key, value in _mapping.items():
        r, g, b = value

        r = r if r > 90 else 0
        g = g if g > 90 else 0
        b = b if b > 90 else 0
        for i in range(-2, 3):
            t = (r+i if r > 50 else 0, g + i if g > 50 else 0, b+i if b > 50 else 0)
            rev_mapp[t] = key

    print('\nReverse Mapping of each character')
    print(rev_mapp)
    return rev_mapp


def coordinates2(start=(0, 50), width=10, height=10, space=2, line_spacing=2, next_line=750):

    coordinate = namedtuple('coordinate', ['x', 'y'])
    start = coordinate(*start)
    upper_left = coordinate(*start)
    lower_right = coordinate(start.x + width, start.y + height)

    while True:
        # check if we need next box in next line
        if upper_left.x > next_line:
            upper_left = coordinate(start.x, upper_left.y + height + line_spacing)
            lower_right = coordinate(start.x + width, lower_right.y + height + line_spacing)

        # first coordinate and so on
        upper_left = coordinate(upper_left.x + width + space, upper_left.y + 0)
        lower_right = coordinate(lower_right.x + width + space, lower_right.y + 0)

        yield upper_left, lower_right


def coordinates(start=(0, 50), width=10, height=10, space=2, line_spacing=2, next_line=750):
    upper_left = start
    lower_right = start[0] + width, start[1] + height

    while True:
        if upper_left[0] > next_line:
            upper_left = start[0], upper_left[1] + height + line_spacing
            lower_right = start[0] + width, lower_right[1] + height + line_spacing

        upper_left = upper_left[0] + width + space, upper_left[1] + 0
        lower_right = lower_right[0] + width + space, lower_right[1] + 0

        yield upper_left, lower_right
