import os
import re
import shutil
from os import listdir
from os.path import isfile, join
#onlyfiles = [f for f in listdir('E:\Python_Udemy_Course\ABC') if isfile(join('E:\Python_Udemy_Course\ABC', f))]
src = 'E:\Python_Udemy_Course\Resumes'
dstn = 'E:\Python_Udemy_Course\Java'
files = []
for filename in [f for f in listdir(src) if isfile(join(src, f))]:
     x = open(os.path.join(src, filename),'r',encoding="utf8")
     y = x.read()
     content = y.splitlines()
     for i in range(0,len(content)):
         text_match = re.findall(r"java",content[i])
         print(text_match)
         if text_match:
            x = filename
            print(x)
            print('hi')
            print(listdir(src))
            if x in listdir(src): 
               print(x)
               src_file = os.path.join(src, x)
               dst_file = os.path.join(dstn, x)
               shutil.move(src_file, dst_file)
     
               


   