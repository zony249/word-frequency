#--------------------------------------------
#   Name: 
#   ID: 
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise 3: Word Frequency
#-------------------------------------------- 
# FREQ TEMPLATE: ADD YOUR INFORMATION TO ABOVE

# You must determine how to structure your solution.
# Create your functions here and call them from under
# if __name__ == "__main__"!

import sys, os

def safe_open(filename):
    if os.path.isfile(filename):
        f = open(filename, "r")
        return (f)
    else:
        print(filename, "is not a file. Please try again. \n")
        return (None)


def main():

    # Checks for the filename argument.
    try:
        f = safe_open(sys.argv[1])
    except IndexError:
        print("Please include the name of your file as shown: ")
        print("python3 freq.py <filename>")
        return -1
    if len(sys.argv) > 2:
        print("Expected one argument after freq.py. Got %d" % (len(sys.argv)-1))
        return -2 

    if f is None:
        return -3

    cFlag = True
    words = {}
    while cFlag:
        string_line = f.readline()
        if string_line == "":
            cFlag = False
            continue
        list_line = string_line.strip().split()
        for i in list_line:
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1




if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to 
    # this exercise, so you should call your code from here.
    main()
