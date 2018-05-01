# Coded by Emily Sawtelle
# Prg 1 part 4
# Bioinformatics 2018
# since the string starts counting with 0, the 63rd charachter in the sequence is 62, this is my first exon is indexed only until 62


sequence = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
print "Sequence length:" , 
print len(sequence)
exon1 = sequence [0:62]
print '%s' % exon1 
intron1 = sequence [63:90].lower()
print '%s' % intron1 
exon2 = sequence [91:len(sequence)]
print '%s' % exon2 