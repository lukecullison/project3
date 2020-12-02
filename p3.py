import sys
import os
import stat

def readFile(infile, pattern):
    with open(infile) as f:
        lin = 1
        col = 0
        for line in f:
            if pattern in line:
                i = 0
                for char in line:
                    p = pattern[i]
                    if(p == char):
                        if len(pattern) == i + 1:
                            print("line: " + str(lin) + ", column: " + str(col - i))
                            i = 0
                    else:
                        i = 0
                    i += 1
                    col += 1
                col = 0
            lin += 1

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 p3.py "pattern" "file1" "file2" [-c]')
        exit()
    i = 2
    if sys.argv[len(sys.argv) - 1] == '-c':
        while(i < len(sys.argv) - 1):
            p = os.access(sys.argv[i], os.R_OK)
            if p == False:
                os.chmod(sys.argv[i], stat.S_IRGRP)
                os.chmod(sys.argv[i], stat.S_IRUSR)
                os.chmod(sys.argv[i], stat.S_IREAD)
            p = os.access(sys.argv[i], os.R_OK)
            if p == True:
                readFile(sys.argv[i], sys.argv[1])
            else:
                print("Invalid file name or file path")
            i += 1
        exit()
    while(i < len(sys.argv)):
        while(i < len(sys.argv)):
            p = os.access(sys.argv[i], os.R_OK)
            if p == True:
                readFile(sys.argv[i], sys.argv[1])
            else:
                print("Invalid file name or file path")
            i += 1
