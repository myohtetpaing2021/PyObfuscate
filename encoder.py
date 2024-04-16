# -*- coding:utf8 -*-

# Supports python2 & python3
# Name   : PyObfuscate - Simple Python Code Obfuscator
# Author : shayshayblack
# Date   : Wed Apr 17 02:22:22 2024

# Import Modules
import os
import sys
import zlib
import gzip
import lzma
import time
import base64
import marshal
import py_compile

# Select raw_input() or input()
if sys.version_info[0]==2:
    _input = "raw_input('%s')"
elif sys.version_info[0]==3:
    _input = "input('%s')"
else:
    sys.exit("\n Your Python Version is not Supported!")

# Encoding
zlb = lambda in_ : zlib.compress(in_)
b16 = lambda in_ : base64.b16encode(in_)
b32 = lambda in_ : base64.b32encode(in_)
b64 = lambda in_ : base64.b64encode(in_)
gzi = lambda in_ : gzip.compress(in_)
lzm = lambda in_ : lzma.compress(in_)
mar = lambda in_ : marshal.dumps(compile(in_,'<x>','exec'))
note = "\x00#\x00 \x00O\x00b\x00f\x00u\x00s\x00c\x00a\x00t\x00e\x00d\x00 \x00w\x00i\x00t\x00h\x00 \x00P\x00y\x00O\x00b\x00f\x00u\x00s\x00c\x00a\x00t\x00e\x00\n\x00#\x00 \x00h\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00w\x00w\x00w\x00.\x00g\x00i\x00t\x00h\x00u\x00b\x00.\x00c\x00o\x00m\x00/\x00c\x00o\x00d\x00e\x00s\x00-\x00t\x00e\x00a\x00m\x00\n\x00#\x00 \x00h\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00t\x00.\x00m\x00e\x00/\x00c\x00o\x00d\x00e\x00s\x00_\x00t\x00e\x00a\x00m\x00\n\x00#\x00 \x00h\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00t\x00.\x00m\x00e\x00/\x00c\x00o\x00d\x00e\x00s\x00_\x00a\x00m\x00e\x00r\x00\n\x00#\x00 \x00T\x00i\x00m\x00e\x00 \x00:\x00 \x00%\x00s\x00\n\x00#\x00 \x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00-\x00\n\x00\n\x00".format(time.ctime())

def banner(): # Program Banner
    print(' ╔═════════════════════════════════╗\n ║          PyObfuscate            ║\n ║  Simple Python Code Obfuscator  ║\n ║  Author : ShayShayBlack            ║\n ║  Github : Github.com/myohtetpaing2021 ║\n ╚═════════════════════════════════╝\n')

def menu(): # Program Menu
    print("\n \x00[\x000\x001\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00\n\x00 \x00[\x000\x002\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00Z\x00l\x00i\x00b\x00\n\x00 \x00[\x000\x003\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00B\x00a\x00s\x00e\x001\x006\x00\n\x00 \x00[\x000\x004\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00B\x00a\x00s\x00e\x003\x002\x00\n\x00 \x00[\x000\x005\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00B\x00a\x00s\x00e\x006\x004\x00\n\x00 \x00[\x000\x006\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00L\x00z\x00m\x00a\x00\n\x00 \x00[\x000\x007\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00G\x00z\x00i\x00p\x00\n\x00 \x00[\x000\x008\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00Z\x00l\x00i\x00b\x00,\x00B\x00a\x00s\x00e\x001\x006\x00\n\x00 \x00[\x000\x009\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00Z\x00l\x00i\x00b\x00,\x00B\x00a\x00s\x00e\x003\x002\x00\n\x00 \x00[\x001\x000\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00Z\x00l\x00i\x00b\x00,\x00B\x00a\x00s\x00e\x006\x004\x00\n\x00 \x00[\x001\x001\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00G\x00z\x00i\x00p\x00,\x00B\x00a\x00s\x00e\x001\x006\x00\n\x00 \x00[\x001\x002\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00G\x00z\x00i\x00p\x00,\x00B\x00a\x00s\x00e\x003\x002\x00\n\x00 \x00[\x001\x003\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00G\x00z\x00i\x00p\x00,\x00B\x00a\x00s\x00e\x006\x004\x00\n\x00 \x00[\x001\x004\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00L\x00z\x00m\x00a\x00,\x00B\x00a\x00s\x00e\x001\x006\x00\n\x00 \x00[\x001\x005\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00L\x00z\x00m\x00a\x00,\x00B\x00a\x00s\x00e\x003\x002\x00\n\x00 \x00[\x001\x006\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00L\x00z\x00m\x00a\x00,\x00B\x00a\x00s\x00e\x006\x004\x00\n\x00 \x00[\x001\x007\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00\n\x00 \x00[\x001\x008\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00G\x00z\x00i\x00p\x00\n\x00 \x00[\x001\x009\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00L\x00z\x00m\x00a\x00\n\x00 \x00[\x002\x000\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00B\x00a\x00s\x00e\x001\x006\x00\n\x00 \x00[\x002\x001\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00B\x00a\x00s\x00e\x003\x002\x00\n\x00 \x00[\x002\x002\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00B\x00a\x00s\x00e\x006\x004\x00\n\x00 \x00[\x002\x003\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00B\x001\x006\x00\n\x00 \x00[\x002\x004\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00B\x003\x002\x00\n\x00 \x00[\x002\x005\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00B\x006\x004\x00\n\x00 \x00[\x002\x006\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00L\x00z\x00m\x00a\x00,\x00B\x001\x006\x00\n\x00 \x00[\x002\x007\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00L\x00z\x00m\x00a\x00,\x00B\x003\x002\x00\n\x00 \x00[\x002\x008\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00L\x00z\x00m\x00a\x00,\x00B\x006\x004\x00\n\x00 \x00[\x002\x009\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00G\x00z\x00i\x00p\x00,\x00B\x001\x006\x00\n\x00 \x00[\x003\x000\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00G\x00z\x00i\x00p\x00,\x00B\x003\x002\x00\n\x00 \x00[\x003\x001\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00G\x00z\x00i\x00p\x00,\x00B\x006\x004\x00\n\x00 \x00[\x003\x002\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00L\x00z\x00m\x00a\x00,\x00B\x001\x006\x00\n\x00 \x00[\x003\x003\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00L\x00z\x00m\x00a\x00,\x00B\x003\x002\x00\n\x00 \x00[\x003\x004\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00L\x00z\x00m\x00a\x00,\x00B\x006\x004\x00\n\x00 \x00[\x003\x005\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00G\x00z\x00i\x00p\x00,\x00B\x001\x006\x00\n\x00 \x00[\x003\x006\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00G\x00z\x00i\x00p\x00,\x00B\x003\x002\x00\n\x00 \x00[\x003\x007\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00G\x00z\x00i\x00p\x00,\x00B\x006\x004\x00\n\x00 \x00[\x003\x008\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00L\x00z\x00m\x00a\x00,\x00G\x00z\x00i\x00p\x00,\x00B\x001\x006\x00\n\x00 \x00[\x003\x009\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00L\x00z\x00m\x00a\x00,\x00G\x00z\x00i\x00p\x00,\x00B\x003\x002\x00\n\x00 \x00[\x004\x000\x00]\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00 \x00M\x00a\x00r\x00s\x00h\x00a\x00l\x00,\x00Z\x00l\x00i\x00b\x00,\x00L\x00z\x00m\x00a\x00,\x00G\x00z\x00i\x00p\x00,\x00B\x006\x004\x00\n\x00 \x00[\x004\x001\x00]\x00 \x00S\x00i\x00m\x00p\x00l\x00e\x00 \x00E\x00n\x00c\x00o\x00d\x00e\x00\n\x00 \x00[\x004\x002\x00]\x00 \x00E\x00x\x00i\x00t\x00\n\x00\n\x00")

class FileSize: # Gets the File Size
    def datas(self,z):
        for x in ['Byte','KB','MB','GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z,x)
            z /= 1024.0
    def __init__(self,path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [-] Encoded File Size : %s\n" % self.datas(dts))
# FileSize('rec.py')

# Encode Menu
def Encode(option,data,output):
    loop = int(eval(_input % " [-] Encode Count : "))
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "lzm(data.encode('utf8')[::-1]"
        heading = "_ = lambda __ : __import__('lzma').decompress(__[::-1]);"
    elif option == 7:
        xx = "gzi(data.encode('utf8')[::-1]"
        heading = "_ = lambda __ : __import__('gzip').decompress(__[::-1]);"
    elif option == 8:
        xx = "b16(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 9:
        xx = "b32(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"
    elif option == 10:
        xx = "b64(zlb(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"
    elif option == 11:
        xx = "b16(gzi(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('gzip').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 12:
        xx = "b32(gzi(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('gzip').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 13:
        xx = "b64(gzi(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('gzip').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 14:
        xx = "b16(lzm(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('lzma').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 15:
        xx = "b32(lzm(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('lzma').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 16:
        xx = "b64(lzm(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('lzma').decompress(__import__('base64').b16decode(__[::-1]));"
    elif option == 17:
        xx = "zlb(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"
    elif option == 18:
        xx = "gzi(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__[::-1]));"
    elif option == 19:
        xx = "lzm(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__[::-1]));"
    elif option == 20:
        xx = "b16(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"
    elif option == 21:
        xx = "b32(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"
    elif option == 22:
        xx = "b64(mar(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"
    elif option == 23:
        xx = "b16(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 24:
        xx = "b32(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 25:
        xx = "b64(zlb(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"
    elif option == 26:
        xx = "b16(lzm(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 27:
        xx = "b32(lzm(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 28:
        xx = "b64(lzm(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('base64').b64decode(__[::-1])));"
    elif option == 29:
        xx = "b16(gzi(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('base64').b16decode(__[::-1])));"
    elif option == 30:
        xx = "b32(gzi(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('base64').b32decode(__[::-1])));"
    elif option == 31:
        xx = "b64(gzi(mar(data.encode('utf8'))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('base64').b64decode(__[::-1])));"
    elif option == 32:
        xx = "b16(zlb(lzm(mar(data.encode('utf8')))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1]))));"
    elif option == 33:
        xx = "b32(zlb(lzm(mar(data.encode('utf8')))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1]))));"
    elif option == 34:
        xx = "b64(zlb(lzm(mar(data.encode('utf8')))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1]))));"
    elif option == 35:
        xx = "b16(zlb(gzi(mar(data.encode('utf8')))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1]))));"
    elif option == 36:
        xx = "b32(zlb(gzi(mar(data.encode('utf8')))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1]))));"
    elif option == 37:
        xx = "b64(zlb(gzip(mar(data.encode('utf8')))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1]))));"
    elif option == 38:
        xx = "b16(zlb(lzm(gzi(mar(data.encode('utf8'))))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))));"
    elif option == 39:
        xx = "b32(zlb(lzm(gzi(mar(data.encode('utf8'))))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))));"
    elif option == 40:
        xx = "b64(zlb(lzm(gzi(mar(data.encode('utf8'))))))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))));"
    else:
        sys.exit("\n Invalid Option!")
    
    for x in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as s:
            sys.exit(" TypeError : " + str(s))
    with open(output, 'w') as f:
        f.write(note + heading + data)
        f.close()

# Special Encode
def SEncode(data,output):
    for x in range(5):
        method = repr(b64(zlb(lzm(gzi(mar(data.encode('utf8'))))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    with open(output, 'w') as f:
        f.write(str(note) + "exec(str(chr(35)%s));" % '+chr(1)'*10000)
        f.write(sata)
        f.close()
    py_compile.compile(output,output)

# Main Menu
def MainMenu():
    try:
        os.system('clear') # os.system('cls')
        banner()
        menu()
        try:
            option = int(eval(_input % " [-] Option : "))
        except ValueError:
            sys.exit("\n Invalid Option !")
        
        if option > 0 and option <= 42:
            if option == 42:
                sys.exit("\n Thanks For Using this Tool")
            os.system('clear') # os.system('cls')
            banner()
        else:
            sys.exit('\n Invalid Option !')
        try:
            file = eval(_input % " [-] File Name : ")
            data = open(file).read()
        except IOError:
            sys.exit("\n File Not Found!")
        
        output = file.lower().replace('.py', '') + '_enc.py'
        if option == 41:
            SEncode(data,output)
        else:
            Encode(option,data,output)
        print("\n [-] Successfully Encrypted %s" % file)
        print(" [-] Saved as %s" % output)
        FileSize(output)
    except KeyboardInterrupt:
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    MainMenu()
