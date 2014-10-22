def b642hex(b64string):
	return b64string.decode('base64','strict').encode('hex')
