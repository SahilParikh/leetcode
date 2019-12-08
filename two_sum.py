def twosum(numarray, num):
    '''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice
    '''
    index_array = []
    for i in numarray:
        addend = abs(num-i)
        if addend in numarray:
            index_array.append([numarray.index(i), numarray.index(addend)])
    return(index_array)


twosum([2,7,11,15], 9)
