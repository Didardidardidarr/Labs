import os
pt = os.path.dirname(os.path.abspath(__file__))
extension = '.py'
every = os.listdir(pt)
for files in every:
    if files.endswith(extension):
        print(files)