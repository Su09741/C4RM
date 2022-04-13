

def FizzBuzz(start, finish):
    v = []
    for i in range(start, finish + 1):
        if i % 15 == 0:
            v.append("FizzBuzz")
        elif i % 5 == 0:
            v.append("Buzz")
        elif i % 3 == 0:
            v.append("Fizz")
        else:
            v.append(str(i))
    return(v)