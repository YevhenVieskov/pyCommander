# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:35:09 2023

@author: Yevhen_Vieskov
"""
#https://www.blog.pythonlibrary.org/2021/09/02/creating-a-file-search-gui-with-wxpython/
#https://github.com/israel-dryer/File-Search-Engine
#https://github.com/akulagrawal/File-Search-Engine
#https://www.opensourceforu.com/2016/10/file-search-with-python/
#https://bart.degoe.de/building-a-full-text-search-engine-150-lines-of-code/
#https://medium.com/analytics-vidhya/search-engine-in-python-from-scratch-c3f7cc453250
#https://courses.cs.washington.edu/courses/cse163/20sp/hw4/spec.html
import os

def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

print(find_files("smpl.htm","D:"))


# Python code to search .mp3 files in current
# folder (We can change file type/name and path
# according to the requirements.
import os
 
# This is to get the directory that the program
# is currently running in.
dir_path = os.path.dirname(os.path.realpath(__file__))
 
for root, dirs, files in os.walk(dir_path):
    for file in files:
 
        # change the extension from '.mp3' to
        # the one of your choice.
        if file.endswith('.mp3'):
            print (root+'/'+str(file))
            
            
            
import glob
 
files = glob.glob('*.mp3')
for file in files:
    print(file)
    
    
