#Import a module 

import os 
d=os.getcwd() #Saved current directory to d 
print(f'Current: {d}')

os.chdir('..') #Changed the directory to its parent directory 
print(f'Current: {os.getcwd()}')
os.chdir(d) #Changed from parent directory to initially how it was 
print(f'Current: {os.getcwd()}')

#ListDir | Lists files 
for f in os.listdir():
    print(f)
    print(f'Path:{os.path.abspath(f)}')
    if os.path.isdir(f): print(f'Dir: {f}')
    if os.path.isfile(f): print(f'File: {f}')
    if os.path.islink(f): print(f'Link: {f}')


#ScanDir 
for e in os.scandir():
    print(e)
    print(f'Name: {e.name}')
    print(f'Path: {e.path}')
    if e.is_dir(): print(f'Dir: {e.name}')
    if e.is_file(): print(f'File: {e.name}')
    if e.is_symlink(): print(f'Link: {e.name}')


