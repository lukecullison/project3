This project parses files to find a specific string pattern specified by the user.
The user inputs files in quotation marks as well as a string pattern in quotation marks as command line arguments
For each file, the program outputs the line and column number each string pattern was found at, and nothing if there were no matches found.
At the end of each file, the program outputs how many matching patterns were found.
After all the files are parsed, the program outputs how many total matches were found in all the files.
If the user inputs a -c argument as the last command line argument, the program modifies the owner, group, and other read permissions for each file that cannot be read from.
If -c was not used as an argument, the program outputs that no file permissions were modified.
If the -c flag was used, but no file permissions needed to be modified, the program outputs that no file permissions were modified.
If the -c flag was used and there were file permissions modified, the program outputs which file permissions were modified.
The following text shows an example for how to run the program.

Usage: python3 p3.py "pattern" "file1" "file2" [-c]
