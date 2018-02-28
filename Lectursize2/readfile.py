f = open('sequence.txt')
data = f.read().rstrip("\n")
lowerSeq = data.lower()
seqLen = len(data)

f2 = open('output.txt', 'w')
f2.write("Original sequence: " + data + "\n")
f2.write("Lowercase sequence: " + lowerSeq + "\n")
f2.write("Length of sequence: " + str(seqLen) + "\n")

f2.close()