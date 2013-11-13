# -*- coding: utf-8 -*- 

'''
Created on 2013-11-13

@author: gjwang
'''

import sys
import hashlib
import zlib
import binascii
import time

def md5sum(filename):
    md5 = hashlib.md5()
    try:
        with open(filename,'rb') as f: 
            for chunk in iter(lambda: f.read(128*md5.block_size), b''): 
                md5.update(chunk)
    except EnvironmentError as exc:
        print exc        
        return '0'
    else:
        return md5.hexdigest()

def crc32sum(filename):
    crc = 0
    crc32 = zlib.crc32
    #crc32 = binascii.crc32
    try:
        with open(filename,'rb') as f: 
            for chunk in iter(lambda: f.read(8192), b''): 
                crc = crc32(chunk, crc)
    except EnvironmentError as exc:
        print exc        
        return '0'
    else:
        return "%x"%(crc & 0xFFFFFFFF)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "usage: crc32_vs_md5.py filename"
        exit(0)
    else:
        filename = sys.argv[1]

    bt = time.time()
    print md5sum(filename)
    et = time.time()
    print "md5 used time: %s" % (et - bt)

    bt2 = time.time()
    print crc32sum(filename)
    et2 = time.time()
    print "crc used time: %s"%(et2 - bt2)
