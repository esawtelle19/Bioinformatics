# coded by Emily Sawtelle
# Program 1 part 3 
#bioinformatics 2018
# DNA = ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT

print "Please enter DNA sequence: ", 
DNA = raw_input()
sequence = DNA.upper()
compliment = sequence.replace('A', 't')
compliment = compliment.replace('T', 'a')
compliment = compliment.replace('C', 'g')
compliment = compliment.replace('G', 'c')
Uppercompliment = compliment.upper()
print "Compliment sequence is:" ,
print '%s' % Uppercompliment