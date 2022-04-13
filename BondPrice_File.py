

def getBondPrice(y, face, couponRate, m, ppy=1):
    value = 0
    for i in range(1, m*ppy + 1):
        value = (face * (couponRate/ppy))/ ((1 + y) ** i) + value
    value = value + face / ((1 + y) ** m)
    return(value)