# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:22:45 2023

@author: Yevhen_Vieskov
"""
from __future__ import print_function
import psutil
import os
print (os.popen("fsutil fsinfo drives").readlines())
#import psutil
#print(psutil.disk_partitions())



dps = psutil.disk_partitions()
fmt_str = "{:<8} {:<7} {:<7}"
print(fmt_str.format("Drive", "Type", "Opts"))
# Only show a couple of different types of devices, for brevity.
for i in range(len(dps)):
    dp = dps[i]
    print(fmt_str.format(dp.device, dp.fstype, dp.opts))
    
# https://stackoverflow.com/questions/12672981/python-os-independent-list-of-available-storage-devices    
import subprocess
import sys

#on windows
#Get the fixed drives
#wmic logicaldisk get name,description
if 'win' in sys.platform:
    drivelist = subprocess.Popen('wmic logicaldisk get name,description', shell=True, stdout=subprocess.PIPE)
    drivelisto, err = drivelist.communicate()
    driveLines = drivelisto.split('\n')
elif 'linux' in sys.platform:
     listdrives=subprocess.Popen('mount', shell=True, stdout=subprocess.PIPE)
     listdrivesout, err=listdrives.communicate()
     for idx,drive in enumerate(filter(None,listdrivesout)):
         listdrivesout[idx]=drive.split()[2]
# guess how it should be on mac os, similar to linux , the mount command should 
# work, but I can't verify it...
elif 'macosx' ...
     do the rest....  
  
  
# https://stackoverflow.com/questions/7718411/determine-device-of-filesystem-in-python
import os

def main():
    dev = os.stat("/home/").st_dev
    major, minor = os.major(dev), os.minor(dev)

    print "/proc/partitions says:", ask_proc_partitions(major, minor)
    print "HAL says:", ask_hal(major, minor)
    print "/sys says:", ask_sysfs(major, minor)

def _parse_proc_partitions():
    res = {}
    for line in file("/proc/partitions"):
        fields = line.split()
        try:
            tmaj = int(fields[0])
            tmin = int(fields[1])
            name = fields[3]
            res[(tmaj, tmin)] = name
        except:
            # just ignore parse errors in header/separator lines
            pass

    return res

def ask_proc_partitions(major, minor):
    d = _parse_proc_partitions()
    return d[(major, minor)]

def ask_hal(major, minor):
    import dbus

    bus = dbus.SystemBus()
    halobj = bus.get_object('org.freedesktop.Hal', '/org/freedesktop/Hal/Manager')
    hal = dbus.Interface(halobj, 'org.freedesktop.Hal.Manager')

    def getdevprops(p):
        bdevi = dbus.Interface(bus.get_object('org.freedesktop.Hal', p),
                               "org.freedesktop.Hal.Device")
        return bdevi.GetAllProperties()

    bdevs = hal.FindDeviceByCapability("block")
    for bdev in bdevs:
        props = getdevprops(bdev)
        if (props['block.major'], props['block.minor']) == (major, minor):
            parentprops = getdevprops(props['info.parent'])
            return (str(props['block.device']), 
                    str(parentprops['block.device']))

def ask_sysfs(major, minor):
    from glob import glob
    needle = "%d:%d" % (major, minor)

    files = glob("/sys/class/block/*/dev")
    for f in files:
        if file(f).read().strip() == needle:
            return os.path.dirname(f)

    return None

if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/3596485/cross-platform-way-to-list-disk-drives-on-linux-windows-and-mac-using-python
import psutil
psutil.disk_partitions()

   
    
"""    
Drive    Type    Opts
C:\      NTFS    rw,fixed
E:\      CDFS    ro,cdrom
"""

'''disk-imaging
floppy-disks
optical-media
python
tapes'''
       
#  https://github.com/ram-jayapalan/filesplit       
#  https://stackoverflow.com/questions/46076754/use-package-from-github-in-conda-virtual-environment  
#  https://stackoverflow.com/questions/62909774/installing-a-package-from-git-in-anaconda-environment-which-is-afterwards-not-re
# https://www.reddit.com/r/learnpython/comments/lmv46f/install_package_in_github_into_a_conda_environment/

# https://docs.anaconda.com/free/anacondaorg/user-guide/tasks/work-with-packages/
# https://gist.github.com/atifraza/b1a92ae7c549dd011590209f188ed2a0

#https://docs.pyfilesystem.org/en/latest/guide.html#opening-filesystems


# https://towardsdatascience.com/10-python-file-system-methods-you-should-know-799f90ef13c2
# https://towardsdatascience.com/7-common-file-system-operations-you-can-do-with-python-e4670c0d92f2
# https://docs.python.org/3/library/archiving.html
# https://docs.python.org/3/library/filesys.html

# https://github.com/ram-jayapalan/filesplit

# https://www.programcreek.com/python/?CodeExample=list+devices

'''import os

import psutil

import shutil

import pathlib

os.chdir("~")

os.chdir("/home/uuu")

os.fspath("/home/uuu")


os.rename("file2.txt","file3.txt")
-

os.remove(“file-name”)
  

os.rmdir(“directory name”)
  

print(os.listdir())

from pathlib import Path

Path.cwd()


import zipfile

with zipfile.ZipFile("sample.zip", mode="r") as archive:
...     archive.printdir()
    
-
try:
...     with zipfile.ZipFile("sample.zip") as archive:
...         archive.printdir()
... except zipfile.BadZipFile as error:
...     print(error)

if zipfile.is_zipfile("sample.zip"):
...     with zipfile.ZipFile("sample.zip", "r") as archive:
...         archive.printdir()
... else:
...     print("File is not a zip file")
    


with zipfile.ZipFile("hello.zip", mode="w") as archive:
...     archive.write("hello.txt")
---------------------------------------------------------------------------


with zipfile.ZipFile("hello.zip", mode="a") as archive:
...     archive.write("new_hello.txt")


with zipfile.ZipFile("hello.zip") as archive:
...     archive.printdir()
File Name                                             Modified             Size

with zipfile.ZipFile("sample.zip", mode="r") as archive:
...     info = archive.getinfo("hello.txt")
    


import datetime

with zipfile.ZipFile("sample.zip", mode="r") as archive:
...     for info in archive.infolist():
...         print(f"Filename: {info.filename}")
...         print(f"Modified: {datetime.datetime(*info.date_time)}")
...         print(f"Normal size: {info.file_size} bytes")
...         print(f"Compressed size: {info.compress_size} bytes")
...         print("-" * 20)

with zipfile.ZipFile("sample.zip", mode="r") as archive:
...     for filename in archive.namelist():
...         print(filename)


with zipfile.ZipFile("sample.zip", mode="r") as archive:
...     for line in archive.read("hello.txt").split(b"\n"):
...         print(line)

with zipfile.ZipFile("sample_pwd.zip", mode="r") as archive:
...     for line in archive.read("hello.txt").split(b"\n"):
...         print(line)

import zipfile

>>> with zipfile.ZipFile("sample_pwd.zip", mode="r") as archive:
...     archive.setpassword(b"secret")
...     for file in archive.namelist():
...         print(file)
...         print("-" * 20)
...         for line in archive.read(file).split(b"\n"):
...             print(line)
 
with zipfile.ZipFile("sample_file_pwd.zip", mode="r") as archive:
...     for line in archive.read("lorem.md", pwd=b"secret2").split(b"\n"):
...         print(line)

'''