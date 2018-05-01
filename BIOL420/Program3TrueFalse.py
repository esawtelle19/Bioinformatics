# Programmed by Emily Sawtelle
# This is for bioinformtics Program 3



import ATcountupdate

sequence = open("data.csv")
for line in sequence:
    column = line.rstrip("\n").split(',')
#important to note where the line splits so only AT content is being looked at and not all information in file given
    species = column[0]
    sequence = column[1]
    genename = column[2]
    expression = column [3]
    ATcontent = ATcountupdate.ATContent(sequence)
    if (ATcountupdate.HighAT(sequence)):
        print "This species %s has a High AT Content" %species 
#This identifies which has what AT Content when printed 
    elif(ATcountupdate.MediumAT(sequence)):
        print "This species %s has a Medium AT Content" %species 
    elif (ATcountupdate.LowAT(sequence)):
        print "This species %s has a Low AT Content" %species 
        
    
# program only counts AT content to determine if it is High, Medium, or low based on Program ATcountupdate
# after else there is no need to indicate a range because this encompasses all that is not true about the other statements   
#high - that takes a sequence and returns True if the sequence has a high AT Content x > 0.65.
#medium - that takes a sequence and returns True if the sequence has a medium, AT Content 0.45 > x < 0.65.
#low - that takes a sequence and returns True if the sequence has a low AT Content x <0.45.