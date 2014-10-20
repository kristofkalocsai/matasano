import fixedxor
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '
def sbxorcip(string):
    messagelist={}
    for c in alphabet:
        keycandid=''
        for x in range(0,(len(string)/2)+1):
            keycandid += str(hex(ord(c))[2:])
        if len(keycandid) != len(string):
            keycandid = keycandid[0:(len(string))]
        decodedhex=fixedxor.fixedxor(string,keycandid)
        charbuff=''
        message=''
        for c in decodedhex:
            charbuff += c
            if len(charbuff) == 2:
                message += chr(int(charbuff,16))
                charbuff = ''
        messagelist[message] = score(message)
    print 'Original: ',string
    print 'Deciphered: '
    return max(messagelist, key=messagelist.get)

def score(string):
    score = 0.0
    for c in alphabet:
        score += string.count(c)
    return score / len(string)
