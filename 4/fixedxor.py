def fixedxor(str1, str2):
    # print str1, str2
    if len(str1) == len(str2):
        return hex(int(str1, 16) ^ int(str2, 16))[2:].rstrip("L")
    else:
        print 'input lengths not equal'
