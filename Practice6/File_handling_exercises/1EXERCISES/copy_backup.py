import shutil
import os
dataa = 'File_handling_exercises/data'
data11 = 'File_handling_exercises/data1'
backupp = 'second_folder'
shutil.copytree(dataa, os.path.join(backupp, dataa))
shutil.copytree(data11, os.path.join(backupp, data11))

