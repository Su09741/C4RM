
def getBondDuration(y, face, couponRate, m, ppy = 1):
    duration = ((1+y) / (ppy*y)) - ( (1 + y + m*(couponRate-y)) / ((ppy*couponRate* ((1+y)**m - 1)) + ppy*y) )
    return(duration)