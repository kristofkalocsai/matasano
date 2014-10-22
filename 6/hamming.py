def hamming(str1,str2):
	str1 = ''.join([bin(int(l,16))[2:].zfill(4) for l in str1])	#hex to binary
	str2 = ''.join([bin(int(l,16))[2:].zfill(4) for l in str2])
	distance = 0																#necessary?
	if len(str1) > len(str2):													#padding with zeroes
		str2 = str2.zfill(len(str1))
	if len(str2) > len(str1):
		str1 = str1.zfill(len(str2))
	for x in range(len(str1)):
		if str1[x] != str2[x]:
			distance += 1
	return distance
