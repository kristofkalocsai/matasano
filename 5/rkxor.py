import fixedxor
def rkxor(plaintext,key):
	hextext = plaintext.encode('hex')
	keyfrag = key.encode('hex')
	for x in range(len(hextext)):
		keyfrag += keyfrag
		if len(keyfrag)>len(hextext):
			break
	keyfrag = keyfrag[:len(hextext)]
	return fixedxor.fixedxor(hextext,keyfrag).zfill(len(hextext))
