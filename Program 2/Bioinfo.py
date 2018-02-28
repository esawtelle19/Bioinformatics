#This code is Assignment 2 written by Emily Sawtelle for Bioinformatics 2018
#name of function is PctofProtien because that is what was given 


def PctOfProtein(Protein, codes):
    Protein=Protein.upper()
    x=0 
    for ll in codes:
        ll=ll.upper()
        x = x+Protein.count(ll)
    return(x/float(len(Protein))*100)

#ll - I chose to use l to represent any letter ll=letter
#x - I chose to use x because I like this letter and its a commmon variable  
#This code was run through Program2Test to ensure that it had worked 
#the answers that were returned were correct 
#line 6 and 8/9 ensure that all code is recognized, no case sensitivity 