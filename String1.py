import string


def donuts(count):
    if count >= 10:
        return "Number of donuts: many"
    else:
        return "Number of donuts: " + str(count)


def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[len(s)-2:]


x = 'Vincent'
both_ends(x)


def fix_start(s):
    first_char = s[0]
    rest = s[1:]
    tmp = rest.replace(first_char, '*')
    return first_char + tmp


def mix_up(a, b):
    a_swapped = b[:2] + a[2:]
    b_swapped = a[:2] + b[2:]
    return a_swapped + ' ' + b_swapped


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():

    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


if __name__ == '__main__':
    main()
def test():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    toto = [[row[i] for row in matrix] for i in range(4)]
    print(toto)
    return toto
test()
#[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

