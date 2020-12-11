import sys
import re
import queue

def get_data(filename):
    file = open(filename, "r")
    data = [int(re.sub("\n", "", line)) for line in file.readlines()]
    return(data)



def main(filename):
    data = get_data(filename)

main(sys.argv[1])