

def getBondPrice_E(face, couponRate, m, yc):
    value = 0
    for i in range(1, m + 1):
        value = (face * couponRate)/ ((1 + yc[i-1]) ** i) + value
    value = value + face / ((1 + yc[len(yc)-1]) ** m)
    return(value)
