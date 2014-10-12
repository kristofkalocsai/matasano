def hextobase64(hexstring):
    hexlist=[ord(c) for c in hexstring]                 #make a list of character orders(ascii codes)
    binlist=[bin(l)[2:].zfill(8) for l in hexlist]      #convert the list to binary values
    binary=''.join(binlist)                             #concat the list so is is one string
    index=[]
    return binary
