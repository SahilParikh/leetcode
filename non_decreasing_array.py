def non_dec_array(array):
    '''
    Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
    We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
    '''
    i = 0
    counter = 0
    while i < len(array):
        if i != len(array) - 1:
            if array[i] > array[i + 1]:       
                array[i] = array[i+1] - 1
                counter += 1
        else:
            if counter >= 2:
                print('False')
            else:
                if array[i] > array[i-1]: 
                    print('True')
                else:
                    print('False')
        i += 1
        
non_dec_array([4,2,3])
non_dec_array([4,2,1])
non_dec_array([1,2,3])        
        
