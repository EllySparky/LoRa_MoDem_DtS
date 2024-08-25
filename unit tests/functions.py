def encoder(hypothesis):
    s = 0
    for i in range(len(hypothesis)):
        s += hypothesis[len(hypothesis)-1-i]*2**i
    return s


