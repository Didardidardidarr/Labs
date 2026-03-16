import os
import shutil
shutil.copytree('Directory_exercises/2EXERCISES/Name','Directory_exercises/2EXERCISES/Another_name/code1')
import os,shutil
b=os.path.dirname(os.path.abspath(__file__))
s=os.path.join(b,'Name','file')
d=os.path.join(b,'Another_name')
if os.path.exists(s):
 shutil.move(s,d)
else:
 print(f"Not found: {s}")