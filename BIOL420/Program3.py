#high - that takes a sequence and returns True if the sequence has a high AT Content x > 0.65.
#medium - that takes a sequence and returns True if the sequence has a medium, AT Content 0.45 > x < 0.65.
#low - that takes a sequence and returns True if the sequence has a low AT Content x <0.45.
# Programmed by Emily Sawtelle
# This is for bioinformtics Program 3
# I updated my ATcount to be similiar to our newer programs so it would work better in this function

import ATcontent
file = open("data.csv", "r")


for line in file:
    gene = line.split(",")
    content = ATcontent.atContent(gene[1])
    if content  > 0.65:
        print gene[0], "High AT Content"
    elif content > 0.45 or content <= 0.65:
        print gene[0], "Medium AT Content"
    else:
        print gene[0], "Low AT Content"


# program only counts AT content to determine if it is High, Medium, or low based on Program ATcountupdate
# after else there is no need to indicate a range because this encompasses all that is not true about the other statements 


