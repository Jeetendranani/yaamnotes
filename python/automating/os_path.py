import os


p = os.path.join('usr', 'bin', 'span')
print(p)

my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(os.path.join('/use/bin/span', filename))

cwd = os.getcwd()
print(cwd)

os.chdir("/Users/yunpengli/PycharmProjects/yaamnotes/python/")
print(os.getcwd())

os.chdir('/Users/yunpengli/PycharmProjects/yaamnotes/python/automating')
print(os.getcwd())

print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

path = '/Users/yunpengli/PycharmProjects/yaamnotes/python/automating/os_path.py'
print(os.path.basename(path))
print(os.path.dirname(path))

print(os.path.split(path))

print(os.path.getsize(path))

total_size = 0
for filename in os.listdir('.'):
    total_size += os.path.getsize(os.path.join(os.path.abspath('.'), filename))

print(total_size)

# todo: shelve module

with open(path) as f:
    print(f.readlines())

