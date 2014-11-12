import b642hex
import hamming
import singlebxorcipher


def rkxbreaker(cipherfile):
    with open(cipherfile, 'r') as f:
        b64ciptext = f.read().replace('\n', '')
        hextext = b642hex.b642hex(b64ciptext)
        # print hextext, '\n'
        ndistances = []
        for keysize in range(2, 44):
            # first keysizeworth:	hextext[:keysize*2]
            # second keysizeworth:	hextext[keysize*2:keysize*4]
            # third keysizeworth:	hextext[keysize*4:keysize*6]
            # fourth keysizeworth:	hextext[keysize*6:keysize*8]
            ndist12 = float(hamming.hamming(hextext[:keysize * 2], hextext[keysize * 2:keysize * 4])) / keysize
            ndist13 = float(hamming.hamming(hextext[:keysize * 2], hextext[keysize * 4:keysize * 6])) / keysize
            ndist14 = float(hamming.hamming(hextext[:keysize * 2], hextext[keysize * 6:keysize * 8])) / keysize
            ndist23 = float(
                hamming.hamming(hextext[keysize * 2:keysize * 4], hextext[keysize * 4:keysize * 6])) / keysize
            ndist24 = float(
                hamming.hamming(hextext[keysize * 2:keysize * 4], hextext[keysize * 6:keysize * 8])) / keysize
            ndist34 = float(
                hamming.hamming(hextext[keysize * 4:keysize * 6], hextext[keysize * 6:keysize * 8])) / keysize
            normdistance = (ndist12 + ndist13 + ndist14 + ndist23 + ndist24 + ndist34) / 6
            # normdistance = float(hamming.hamming(hextext[:keysize*2],hextext[keysize*2:(keysize*4)]))/keysize
            # print hextext[:keysize*2],hextext[keysize*2:(keysize*4)]
            # print hextext[:keysize*2],hextext[keysize*2:keysize*4]
            # print hextext[keysize*4:keysize*6],hextext[keysize*6:keysize*8]
            # if keysize == 40:
            # print len(hextext[:keysize*2]),len(hextext[keysize*2:(keysize*4)])

            # print hamming.hamming(hextext[:(keysize*2)],hextext[(keysize*2):(keysize*4)])
            # print 'keysize: ',keysize,'distance: ', normdistance
            ndistances.append(normdistance)
        KEYSIZE = ndistances.index(min(ndistances)) + 2
        # print 'KEYSIZE: ',KEYSIZE, '\n'
        # TRYING MANUALLY:
        # KEYSIZE = 29
        # print KEYSIZE
        blockbuffer = ''
        blocks = []
        transblocks = []
        plaintblocks = []
        for x in range(KEYSIZE):
            transblocks.append('')
            plaintblocks.append('')
        # print len(transblocks)
        for c in hextext:
            blockbuffer += c
            if len(blockbuffer) == KEYSIZE * 2:
                blocks.append(blockbuffer)
                blockbuffer = ''
        for i in blocks:
            for x in range(KEYSIZE):
                # print x*2,(x*2)+1
                # print i[(x*2):((x*2)+2)]
                transblocks[x] += i[(x * 2):((x * 2) + 2)]
        for i in transblocks:
            # print transblocks.index(i)
            plaintblocks[transblocks.index(i)] = singlebxorcipher.sbxorcip(i)
        plaintext = ''
        for i in range(len(plaintblocks[0])):
            for j in range(KEYSIZE):
                plaintext += (plaintblocks[j][i])
        return plaintext
    # print singlebxorcipher.sbxorcip(i), '\n'
    # print '\n'.join(blocks)
    # print transblocks[0], '\n'
    # print transblocks[1], '\n'
    # print transblocks[2], '\n'
    # print transblocks[3], '\n'
    # print transblocks[4], '\n'
