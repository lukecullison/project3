import sys
import os

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
    #This is random text: randoms
    # pattern = randoms len(randoms) = 7
    path1 = os.access(sys.argv[1], os.R_OK)
    print("Exists the path:", path1)
    readFile(sys.argv[1], sys.argv[2])
