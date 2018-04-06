#prog 4
#bioinfo by emily sawtelle

import re
# re is regular expression in python 

DNA = open("DNA.txt", "r")
for line in DNA:
    
# ABCI = ANT/AAT N = any base
# ABCII = GCXY/TG X= A or G Y= A or T

    all_cuts = [0]
    
#add cut positions for ABCI

    for match in re.finditer(r"A[ATGC]TAAT", line):
        all_cuts.append(match.start() + 3)
        # line above was given - makes sure the line counts all of the sequence 

#add cut positions for ABCII  

    for match in re.finditer(r"GC[AG][AT]TG", line):
         all_cuts.append(match.start() + 4)
         #line above was given - makes sure the entire sequence is counted and cut in the proper place 
         
sortedlist = sorted(all_cuts)

print sortedlist 

print "Fragment size is %s basepairs in length" % (sortedlist[1] - sortedlist[0])
print "Fragment size is %s basepairs in length" % (sortedlist[2] - sortedlist[1])
print "Fragment size is %s basepairs in length" % (sortedlist[3] - sortedlist[2])
print "Fragment size is %s basepairs in length" % (sortedlist[4] - sortedlist[3])
print "Fragment size is %s basepairs in length" % (len(line) - sortedlist[4] - 1)

# each print for length is minus the fragemnet length before it so it can calculate length based on end - start 