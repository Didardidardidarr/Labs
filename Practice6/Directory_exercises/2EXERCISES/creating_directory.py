import os 
directory='Directory_exercises/2EXERCISES/Name/file'
directory1 = 'Directory_exercises/2EXERCISES/Name/code1'
directory2 = "Directory_exercises/2EXERCISES/Another_name/code2"
os.makedirs(directory1)
os.makedirs(directory2)
os.makedirs(directory)
direct1 = open('Directory_exercises/2EXERCISES/Name/code1/textdir1.txt', 'w')
direct2 = open('Directory_exercises/2EXERCISES/Another_name/code2/textdir2.txt', 'w')
direct1.write("Hello world!")
direct2.write("Helloo")
direct1.close()
direct2.close()