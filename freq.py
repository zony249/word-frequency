#--------------------------------------------
#   Name: Zong Lin Yu 
#   ID: 1614934
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise 3: Word Frequency
#-------------------------------------------- 

import sys, os

def safe_open(filename):
    """ Safely opens a file, checking if the file exists.
    If the file does not exist, raises FileNotFoundError.

    Argument:
        filename (str): A string representing
            the path of the file.

    Returns:
        f (file object): A file object where the permission
            is set to "r".
        
    """
    if os.path.isfile(filename):
        f = open(filename, "r")
        return (f)
    else:
        raise FileNotFoundError()

def count_words(file_obj):
    """ Creates a dictionary that stores each unique word
    in the file object as well as its occurance. 

    Arguments:
        file_obj (file object): A file object

    Returns:
        words (dict): A dictionary that contains every
            unique word as well as the number
            of times that word occurs.

    """
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
    h_text = "Usage: python3 freq.py <argument> \n"
    h_text += "    <argument>: \n"
    h_text += "        <filename>: the path of a file \n"
    h_text += "        -h or --help: display this help message\n"
    print(h_text)

def print_freq_tab(dictionary, filename):
    """ Prints the frequency table in the form 
    <word> <occurances> <frequency fraction>
    where:
        <word>: a unique word contained in the dictionary
        <occurances>: the number of times <word> occurs
        <frequency fraction>: <occurances> /(total number of words)

    Arguments:
        dictionary (dict): A dictionary where the keys are the
            words and the values are the number of occurances

        filename (str): The file name of the file that was opened.
            This program saves the output as <filename>.out.
    """
    list_sorted_keys = sorted(dictionary.keys())
    total_count = sum(dictionary.values())
    
    f_out_fname = filename + ".out"
    f_out = open(f_out_fname, "w")

    for i in list_sorted_keys:
        key = i
        value = dictionary[i]
        freq = round(dictionary[i]/total_count, 3)
        print('%s %s %s' % (key, value, freq), file=f_out)
    f_out.close()
    
def main():

    # Checks for the filename argument.
    try:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            hflag()
            return 0
        filename = sys.argv[1]
        f = safe_open(filename)
    except IndexError: # if sys.argv doesn't have index [1]
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
    f.close()
    return 0


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to 
    # this exercise, so you should call your code from here.
    main()
