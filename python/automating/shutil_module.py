import shutil
import os


shutil.move('data1', 'mydata')
shutil.copy('mydata', 'databak')
shutil.move('mydata', 'data1')

"""
- Call os.unlink(path) will delete the file at path
- call os.rmdir(path) will delete the folder at path, the folder must be empty of any files or folders
- call shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.
"""

for filename in os.listdir():
    if filename.endswith('.py'):
        print(filename)


import send2trash


bacon_file = open('bacon.txt', 'a')
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()

shutil.copy('bacon.txt', 'bacon.bak')
send2trash.send2trash('bacon.txt')

print(' ')
for folder_name, subfolders, filenames in os.walk('.'):
    print('The current folder is ' + folder_name)

    for subfolder in subfolders:
        print('Subfolder of ' + folder_name + ': ' + subfolder)

    for filename in filenames:
        print('File inside ' + folder_name + ': ' + filename)

    print(' ')
