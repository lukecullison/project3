import sys
import os

if __name__ == '__main__':
    path1 = os.access(sys.argv[1], os.R_OK)
    print("Exists the path:", path1)
