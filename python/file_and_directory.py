import os


print(os.name)
print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))

print(os.path.abspath('.'))
os.mkdir('/Users/YunpengLi/testdir')
os.rmdir('/Users/yunpengLi/testdir')

print(os.path.join('/Users/YunpengLi', 'testdir'))
print(os.path.split('/Users/yunpengli/PycharmProjects/leetcode/python/hello.py'))
print(os.path.splitext('/Users/yunpengli/PycharmProjects/leetcode/python/hello.py'))

dirlist = [x for x in os.listdir('.') if os.path.isdir(x)]
print(dirlist)

print(os.listdir('./python'))
pyfiles = [x for x in os.listdir('./python') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(pyfiles)

