

def getBondPrice_Z(face, couponRate, times, yc):
    value = 0
    count = 0
    for i in times:
        value = (face * couponRate)/ ((1 + yc[count]) ** i) + value
        count = count + 1
    value = value + face / ((1 + yc[len(yc)-1]) ** times[len(times)-1])
    return(value)