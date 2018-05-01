def atContent (sequence):
    allCaps = sequence.upper()
    aN = allCaps.count('A')
    tN = allCaps.count('T')
    ATContent = (aN + tN) / float(len(allCaps))
    return ATContent