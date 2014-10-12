def hextobase64(hexstring):
    hexlist=[ord(c) for c in hexstring]                 #make a list of character orders(ascii codes)
    binlist=[bin(l)[2:].zfill(8) for l in hexlist]      #convert the list to binary values
    binary=''.join(binlist)                             #concat the list so it is one string
    index='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    base64=''
    charbuff = ''
    for c in binary:
        charbuff += c
        # print len(charbuff)
        # print charbuff
        if len(charbuff) == 6:
            base64 += index[int(charbuff,2)]
            charbuff = ''
    if (len(binary)/8)% 3 == 1:
        base64 += '=='
    if (len(binary)/8)% 3 == 2:
        base64 += '='
    return base64
