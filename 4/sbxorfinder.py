import singlebxorcipher
def sbxorfind(cipherfile):
    with open(cipherfile,'r') as f:
        messagelist={}
        for line in f:
            message = singlebxorcipher.sbxorcip(line)
            messagelist[message] = singlebxorcipher.score(message)
        # print 'The best score: '
        return max(messagelist, key=messagelist.get)
