def non_dec_array(array):
    '''
    Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
    We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
    '''
def non_decr_array(int_list):
    counter = 0
    for i in range(len(int_list)-1):
        if int_list[i] > int_list[i+1]:
            counter += 1
            if i == 0:
                int_list[i] = int_list[i+1]
            else:
                int_list[i+1] = int_list[i]            
    if counter > 1:
        print('False')
    else:
        print('True')


non_decr_array([4,2,1])
non_decr_array([4,2,3])
non_decr_array([4,7,3,5,6])
non_decr_array([4,2,3,5,6])
non_decr_array([13,17,6,20,21])  
non_decr_array([4,134,3,13431,6])
    
        
