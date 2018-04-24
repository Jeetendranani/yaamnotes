f = open('/Users/yunpengli/PycharmProjects/yaamnotes/python/hello.py', 'r')
print(f.read())
f.close()

try:
    f = open('/Users/yunpengli/PycharmProjects/yaamnotes/python/hello.py', 'r')
    print(f.read())

finally:
    if f:
        f.close()

with open('/Users/yunpengli/PycharmProjects/yaamnotes/python/hello.py', 'r') as f:
    print(f.read())


with open('/Users/yunpengli/PycharmProjects/yaamnotes/python/hello.py', 'r') as f:
    for line in f.readlines():
        print(line)

