import b642hex
import fixedxor
import hamming
import singlebxorcipher


def rkxbreaker(cipherfile):
    with open(cipherfile, 'r+') as f:
        # print len(f.read())
        b64ciptext = f.read().replace('\n', '')
        hextext = b642hex.b642hex(b64ciptext)
        # print len(b64ciptext)
        # print hextext, '\n'
        ndistances = []
        for keysize in range(2, 41):
            # first keysizeworth:	hextext[:keysize*2]
            # second keysizeworth:	hextext[keysize*2:keysize*4]
            # third keysizeworth:	hextext[keysize*4:keysize*6]
            # fourth keysizeworth:	hextext[keysize*6:keysize*8]
            hdist12 = float(
                hamming.hamming(hextext[:keysize * 2], hextext[keysize * 2:keysize * 4])) / keysize
            hdist13 = float(
                hamming.hamming(hextext[:keysize * 2], hextext[keysize * 4:keysize * 6])) / keysize
            hdist14 = float(
                hamming.hamming(hextext[:keysize * 2], hextext[keysize * 6:keysize * 8])) / keysize
            hdist23 = float(
                hamming.hamming(hextext[keysize * 2:keysize * 4], hextext[keysize * 4:keysize * 6])) / keysize
            hdist24 = float(
                hamming.hamming(hextext[keysize * 2:keysize * 4], hextext[keysize * 6:keysize * 8])) / keysize
            hdist34 = float(
                hamming.hamming(hextext[keysize * 4:keysize * 6], hextext[keysize * 6:keysize * 8])) / keysize
            normdistance = (hdist12 + hdist13 + hdist14 + hdist23 + hdist24 + hdist34) / 6
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
        # key = ''
        plaintext = ''
        for i in range(len(plaintblocks[0])):
            for j in range(KEYSIZE):
                plaintext += (plaintblocks[j][i])
        # print KEYSIZE
        # plainhex = plaintext.encode('hex')
        # print len(plainhex), len(hextext)
        # key = fixedxor.fixedxor(plainhex,hextext[:len(plainhex)])[:KEYSIZE*2].decode('hex')
        # print key
        # for i in range(KEYSIZE):
        #     key += fixedxor.fixedxor(hextext[(2*i-1):(2*i)], str(ord(plaintext[i])))
        # # print hextext[0],hextext[1], ord(plaintext[0]), ord(plaintext[1])
        return plaintext
    # print singlebxorcipher.sbxorcip(i), '\n'
    # print '\n'.join(blocks)
    # print transblocks[0], '\n'
    # print transblocks[1], '\n'
    # print transblocks[2], '\n'
    # print transblocks[3], '\n'
    # print transblocks[4], '\n'
