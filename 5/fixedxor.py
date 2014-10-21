def fixedxor(str1, str2):
    # print str1,'\n', str2
    if len(str1) == len(str2):
        # print bin(int(str1, 16)).zfill(len(str1)*4)
        # print bin(int(str2, 16)).zfill(len(str2)*4)
        return hex(int(str1, 16) ^ int(str2, 16))[2:].rstrip("L")
    else:
        print 'input lengths not equal'
