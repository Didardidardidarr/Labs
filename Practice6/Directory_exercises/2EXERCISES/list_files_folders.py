import os
pt = 'Directory_exercises/2EXERCISES'
everthng = os.listdir(pt)
for item in everthng:
    if os.path.isdir(item):
        print(f"ПАПКА:{item}")
    else:
        print(f"ФАЙЛ:{item}")