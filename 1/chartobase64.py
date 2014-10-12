def chartobase64(charstring):
    charlist=[ord(c) for c in charstring]                 #make a list of character orders(ascii codes)
    binlist=[bin(l)[2:].zfill(8) for l in charlist]      #convert the list to binary values
    binary=''.join(binlist)                             #concat the list so it is one string
    index='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base64=''                                           #are these necessary?
    charbuff = ''
    for c in binary:
        charbuff += c
        if len(charbuff) == 6:
            base64 += index[int(charbuff,2)]
            charbuff = ''
    if (len(binary)/8)% 3 == 1:                         #padding if necessary
        base64 += '=='
    if (len(binary)/8)% 3 == 2:
        base64 += '='
    return base64
