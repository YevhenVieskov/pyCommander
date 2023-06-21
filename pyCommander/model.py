from pathlib import Path
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class MountVolume:

    def __init__(self, device="", name="", file_system_type="",
                 bytes_free=0, bytes_total=0, size=""):
        self.device = device
        self.name = name
        self.fstype = file_system_type
        self.bytes_free = bytes_free
        self.bytes_total = bytes_total
        self.size


def getDevices():
    marker = 1024.0
    decimal = 2
    kiloBytes = marker  # One Kilobyte is 1024 bytes
    megaBytes = marker * marker  # One MB is 1024 KB
    gigaBytes = marker * marker * marker  # One GB is 1024 MB
    teraBytes = marker * marker * marker * marker  # One TB is 1024 GB

    dlist = []
    mv = MountVolume()
    storage = QtCore.QStorageInfo
    stlist = storage.mountedVolumes()
    n = len(stlist)
    for i in range(n):
        if (stlist[i].isValid() and stlist[i].isReady):
            device = str(stlist[i].device(), "utf-8")
            name = stlist[i].name()
            file_system_type = str(stlist[i].fileSystemType(), "utf-8")
            bytes_free = stlist[i].bytesFree()
            bytes_total = stlist[i].bytesTotal()
            # return bytes if less than a KB
            if (bytes_free < kiloBytes or bytes_total < kiloBytes):
                size = str(bytes_free) + "B" + "/" + str(bytes_total) + "B"
            # return KB if less than a MB
            elif (bytes_free < megaBytes or bytes_total < megaBytes):
                size = str(bytes_free/kiloBytes) + "K" + "/" + \
                    str(bytes_total/kiloBytes) + "K"
            # return MB if less than a GB
            elif (bytes_free < gigaBytes or bytes_total < gigaBytes):
                size = str(bytes_free/megaBytes) + "M" + "/" + \
                    str(bytes_total/megaBytes) + "M"
            # return GB if less than a TB
            elif (bytes_free < teraBytes or bytes_total < teraBytes):
                size = str(bytes_free/gigaBytes) + "G" + "/" + \
                    str(bytes_total/gigaBytes) + "G"
            else:
                size = str(bytes_free/teraBytes) + "T" + "/" + \
                    str(bytes_total/teraBytes) + "T"
        if (file_system_type != "tmpfs" and file_system_type != "squashfs"):
            mv = MountVolume(device, name, file_system_type,
                             bytes_free, bytes_total, size)
            dlist.append(mv)
    return dlist
