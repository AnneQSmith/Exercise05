# import a file
from sys import argv
import os

#print argv
if len(argv) != 2:
    print "Please enter the filename only on the command line. "

else:
    filename = argv[1]
    print filename

    if not os.path.isfile(filename):
        print "Sorry, couldn't find file: ", filename
     
    else:
        twain = open(filename)
    
        ascii_counts = 26*[0]
        
        for line in twain:
            charlist = line.lower()
            for char in charlist:
                if char >= 'a' and char <= 'z':
                    ascii_counts[ord(char) - ord('a')] +=1
       
        twain.close()

        for i in range(len(ascii_counts)):
          print ascii_counts[i]