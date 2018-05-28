import zipfile
import os


example_zip = zipfile.ZipFile('example.zip')
print(example_zip.namelist())