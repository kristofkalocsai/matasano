import b642hex
def rkxbreaker(cipherfile):
	with open(cipherfile,'r') as f:
		b64ciptext = f.read().replace('\n','')
		hextext = b642hex.b642hex(b64ciptext)
		for keysize in range(2,41):
			# print hextext[:keysize*2],'\n',hextext[keysize*2:keysize*4]
