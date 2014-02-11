# import a file
from sys import argv

#print argv
if len(argv) != 2:
    print "Please enter a filname on the command line"

# Sanitization needed -- check for existence of file

else:
    filename = argv[1]
    print filename

    twain = open(filename)
    
    ascii_counts = 26*[0]
    
    for line in twain:
        charlist = line.lower()
        for char in charlist:
            if char >= 'a' and char <= 'z':
                ascii_counts[ord(char) - ord('a')] +=1

    
    for i in range(len(ascii_counts)):
      #  print "There are %d instances of the letter %s" % (ascii_counts[i],str(unichr(97+i)))
      print ascii_counts[i]






 
       # for  char in charlist:
        #    print char

   