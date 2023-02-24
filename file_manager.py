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
       