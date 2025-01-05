---
title: File Challange
---
# RegEx Challange


#open a file and splitting by newlines:
with open("out.txt") as f:
    data = f.read().splitlines()
    print "h\n"
//
#open a file a print out all lines starting with a pattern:
with open("test.fasta") as f:
   for line in f:
       if line.startswith(">"):
           print line,

