line1 = "ABC123"
line2 = "DEF456"
line3 = "HIJ789"

seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq2 = "ACTGATCGACGATCGATCGATCACGACT"
seq3 = "ACTGACACTGTACTGTACATGTG"

output = open("sequence.fasta" , 'w')
output.write ('>' + line1 + '\n' + seq1 + '\n')
output.write ('>' + line2 + '\n' + seq2 + '\n')
output.write ('>' + line3 + '\n' + seq3 + '\n')

output.close()