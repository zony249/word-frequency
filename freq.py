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
        raise FileNotFoundError()

def count_words(file_obj):
    
    cFlag = True
    words = {}
    while cFlag:
        string_line = file_obj.readline()
        if string_line == "":
            cFlag = False
            continue
        list_line = string_line.strip().split()
        for i in list_line:
            if i not in words:
                words[i] = 1
            else:
                words[i] += 1
    return words

def hflag():
    print("help")

def print_freq_tab(dictionary, filename):
    list_sorted_keys = sorted(dictionary.keys())
    total_count = sum(dictionary.values())
    
    f_out_fname = filename + ".out"
    f_out = open(f_out_fname, "w")

    for i in list_sorted_keys:
        key = i
        value = dictionary[i]
        freq = round(dictionary[i]/total_count, 3)
        print('%-15s%-15s%-15s' % (key, value, freq), file=f_out)
    f_out.close()
    
def main():

    # Checks for the filename argument.
    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            hflag()
            return 0
        filename = sys.argv[1]
        f = safe_open(filename)
    except IndexError:
        print("Please include the name of your file as shown: ")
        print("python3 freq.py <filename>")
        return -1
    except FileNotFoundError:
        print(sys.argv[1], "is not a file. Please try again. \n")
        return -1

    if len(sys.argv) > 2:
        print("Expected one argument after freq.py. Got %d" % (len(sys.argv)-1))
        
        return -2 

    words = count_words(f)
    print_freq_tab(words, filename)

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to 
    # this exercise, so you should call your code from here.
    main()
