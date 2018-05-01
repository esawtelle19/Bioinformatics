# Programmed by Emily Sawtelle
# This is for bioinformtics Program 1 
# I thought it would be interesting to be able to use this code, in the future so i decided to use a raw data input for the DNA strand 
# to input in, instead of using the strand given to us. 
# A = A content & T = T content, AT = AT content using equation given 
# DNA = ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT

print "Enter sequence:" , 
DNA = raw_input()
A = DNA.count ('A')
T = DNA.count ('T')
totalbases = len(DNA)
AT = int(A + T)/float(totalbases)
print "AT content in sequence is:" ,
print "%.2f" % AT 