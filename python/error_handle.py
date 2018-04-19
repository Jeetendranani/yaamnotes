import logging


def foo():
    r = some_function()
    if r == -1:
        return -1
    return r


def some_function():
    return 0


def bar():
    r = foo()
    if r == -1:
        print("Error")
    else:
        pass


try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print("END")


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
        logging.exception(e)
    finally:
        print('Finally...')


main()
print('END')

