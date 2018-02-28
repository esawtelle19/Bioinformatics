def atContent(sequence):
    allCaps = sequence.upper()
    aN = allCaps.count('A')
    tN = allCaps.count('T')
    result = (aN + tN) / float(len(allCaps))
    return result