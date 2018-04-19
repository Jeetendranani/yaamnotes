from io import StringIO, BytesIO


f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

f = StringIO("Hello!\nHi!\nGoodbye!")

while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
