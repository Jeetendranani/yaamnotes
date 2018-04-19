import logging
logging.basicConfig(level=logging.INFO)


def foo(s):
    n = int(s)
    print(">>> n = {}".format(n))
    return 10 / n


def main():
    foo('0')


# main()


def foo1(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main1():
    foo1('0')


# main1()


def foo2(s):
    n = int(s)
    logging.info("n = {}".format(n))
    print(10 / n)


def main2():
    foo2('0')


main2()

