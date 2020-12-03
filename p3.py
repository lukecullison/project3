import sys
import os
import stat

def readFile(infile, pattern):
    with open(infile) as f:
        lin = 1
        col = 0
        count = 0
        for line in f:
            if pattern in line:
                i = 0
                for char in line:
                    p = pattern[i]
                    if(p == char):
                        if len(pattern) == i + 1:
                            print(infile + ": found " + pattern + " on line: " + str(lin) + ", column: " + str(col - i))
                            count += 1
                            i = 0
                        else:
                            i += 1
                    else:
                        i = 0
                    col += 1
                col = 0
            lin += 1
        print(infile + ": found " + str(count) + " matching pattern(s)")
        return count
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 p3.py "pattern" "file1" "file2" [-c]')
        exit()
    i = 2
    pcount = 0
    if sys.argv[len(sys.argv) - 1] == '-c':
        changed = False
        while(i < len(sys.argv) - 1):
            p = os.access(sys.argv[i], os.R_OK)
            mod = False
            if p == False:
                os.chmod(sys.argv[i], stat.S_IRGRP)
                os.chmod(sys.argv[i], stat.S_IRUSR)
                os.chmod(sys.argv[i], stat.S_IREAD)
                mod = True
            p = os.access(sys.argv[i], os.R_OK)
            if p == True:
                pcount += readFile(sys.argv[i], sys.argv[1])
                if mod:
                    changed = True
                    print(sys.argv[i] + ": Changed file read permissions for owner, group, and other")
            else:
                print("Invalid file name or file path")
            i += 1
        if changed == False:
            print("No file permissions were modified")
        print("Summary: " + str(pcount) + " matche(s) found in " + str(len(sys.argv) - 3) + " files")
        exit()
    while(i < len(sys.argv)):
        p = os.access(sys.argv[i], os.R_OK)
        if p == True:
            pcount += readFile(sys.argv[i], sys.argv[1])
        else:
            print("Invalid file name or file path")
        i += 1
    print("No file permissions were modified")
    print("Summary: " + str(pcount) + " matche(s) found in " + str(len(sys.argv) - 2) + " files")
