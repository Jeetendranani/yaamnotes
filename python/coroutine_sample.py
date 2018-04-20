def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print("[CONSUMER] consuming {}...".format(n))
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print("[PRODUCER] producing {}...".format(n))
        r = c.send(n)
        print("[PRODUCER] consumer return {}".format(r))
    c.close()


c = consumer()
produce(c)