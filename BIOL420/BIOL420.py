#Programmed by Emily Sawtelle
#April 26, 2018
#For Bioinformtics (BIOL420) Spring 2018

#name of function is PctofProtien because that is what was given 
# line 1 defines the function
# line 2 changes the protein to uppercase so that the code isn't case sensitive
# ll is amino acid and that is changed to upper from the list defined by codes
# x is the number of codes within the protein 
# the program should return the percentage of the list that was in the protein sequence

def PctOfProtein(Protein, codes):
    Protein=Protein.upper()
    x=0 
    for ll in codes:
        ll=ll.upper()
        x = x+Protein.count(ll)
    return(x/float(len(Protein))*100)
    
#line 1 deines program
# line 2 makes all upper
# line 3 counts A
#Line 4 counts T
#line 5/6 figure AT content and return value 


def atContent (sequence):
    allCaps = sequence.upper()
    aN = allCaps.count('A')
    tN = allCaps.count('T')
    ATContent = (aN + tN) / float(len(allCaps))
    return ATContent

#high - that takes a sequence and returns True if the sequence has a high AT Content x > 0.65    
#medium - that takes a sequence and returns True if the sequence has a medium, AT Content 0.45 > x < 0.65.
#low - that takes a sequence and returns True if the sequence has a low AT Content x <0.45.
#this creates a loop so if it is not High AT it will continue to run through the other functions until it is true
#else is used because if the sequence does not have the right AT content match then it cannot be  true

def ATContent (sequence):
    allCaps = sequence.upper()
    aN = allCaps.count('A')
    tN = allCaps.count('T')
    ATContent = (aN + tN) / float(len(allCaps))
    return ATContent

def HighAT(ATContent):
    if ATContent > 0.65:
        return(True)
    else:
        return(False) 
    
def MediumAT (ATContent):
    if ATContent >= 0.45 and ATContent <= 0.65:
        return(True)
    else:
        return(False)

def LowAT (ATContent):
    if ATContent < 0.45:
        return(True)
    else:
        return(False)


#coded for bioinformatics 

gencode = {
 'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
 'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
 
#above was prompted in assignment

def translate_dna(sequence):
    codons=[]
    #codons hold codons
    amnino=[]
    #amino holds amino acids from the dictionary
    codons=[sequence[i:i+3] for i in range(0, len(sequence), 3)]
    #splits the string into codons to be read properly
    
    for c in codons:
        amnino.append(gencode.get(c))
    return amnino
    
    #c in loop gets amino acids from the dictionary
    
def atContent(sequence):
    allCaps = sequence.upper()
    aN = allCaps.count('A')
    tN = allCaps.count('T')
    result = (aN + tN) / float(len(allCaps))
    return result
    
def extractExon(dna, start, stop):
    exon = dna[start-1:stop]
    return exon