print "How many malcorps did you find on planet Exflon?",
exflon = raw_input()
print "How many malcorps did you find on planet Mobiles?",
mobiles = raw_input()
print "How many malcorps did you find on planet Monsantoes?",
monstantoes = raw_input()
total = int(exflon) + int(mobiles) + int(monstantoes)
print "You found %s malcorps!" % total
print "The average number of malcorps per planet is %.2f" % (total/3.0)