import sys
import os
import shutil
import struct
KEY = 'a'

def encrypt_file(src, dst):
    filename = os.path.splitext(dst)
    dst_filename = filename[0] + ".pac"
    print src, dst_filename
    srcFile = open(src, "rb")
    destFileContent = ""
    dstFile = open(dst_filename, "wb")
    try:
        while True:
            c = srcFile.read(1)
            if c == "":
                break
            d = ord(c) ^ 0x90
            dstFile.write(struct.pack('b',d))

    finally:
        srcFile.close()

def encrypt_dir(src, dst):
    names = os.listdir(src)
    if not os.path.exists(dst):
        os.mkdir(dst)
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        
        if os.path.isdir(srcname):                
            encrypt_dir(srcname, dstname)
        else:
            if (not os.path.exists(dstname)
                or ((os.path.exists(dstname))
                    and (os.path.getsize(dstname) != os.path.getsize(srcname)))):
                encrypt_file(srcname, dstname)                    

def start():
    destDir = sys.argv[1]
    outputDir = "./Output"
    encrypt_dir(destDir, outputDir)

if __name__ == '__main__':
    start()