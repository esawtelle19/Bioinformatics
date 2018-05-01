# This was coded by Emily Sawtelle 
#Bioinformatics 2018
# Prg 1 Part 2

print 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
seq = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT'
print "Sequence length is: " ,
print len(seq)
loc = seq.find('GAATTC')
print "Location of restriction site:" , 
print loc +1 
print "Fragement Length before ECROI:" , 
print len(seq[0:loc+1])
print "Fragement length after ECORI:" ,
print len(seq[loc +1: len(seq)])

# I wanted to identify the restricition site specifically so that this code could be used in the future
# I made sure to have the length given on the same line as the text to make the code look neater