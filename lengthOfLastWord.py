def lengthOfLastWord(s):
    '''
    Given a string s consists of upper/lower-case alphabets and
    empty space characters ' ', return the length of
    last word (last word means the last appearing word if we loop from
    left to right) in the string.

    If the last word does not exist, return 0
    '''
    newCount = 0
    oldCount = 0
    for i in s:        
        if i != ' ':
            oldCount += 1
        else:
            if oldCount > newCount:
                newCount = oldCount
                oldCount = 0

    print(newCount)
                    
                    
lengthOfLastWord('This is a test lmfaooo')
