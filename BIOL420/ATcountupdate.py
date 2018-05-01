#high - that takes a sequence and returns True if the sequence has a high AT Content x > 0.65.
#medium - that takes a sequence and returns True if the sequence has a medium, AT Content 0.45 > x < 0.65.
#low - that takes a sequence and returns True if the sequence has a low AT Content x <0.45.
# Programmed by Emily Sawtelle
# This is for bioinformtics Program 3
# I updated my ATcount to be similiar to our newer programs so it would work better in this function


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

#this creates a loop so if it is not High AT it will continue to run through the othre functions until it is true
#else is used because if the sequence does not have the right AT content match then it cannot be  true
#AT content values are based upon info given in prompt 