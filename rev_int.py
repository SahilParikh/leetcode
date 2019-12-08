def rev_int(x):
    '''
    Given a 32-bit signed integer, reverse digits of an integer
    
    x = singed 32 bit int
    '''
    orig_num = x
    x = str(abs(x)).rstrip('0')
    rev_str = ''

    if orig_num != 0:
        for i in range(len(x)-1,-1,-1):
            rev_str += x[i]
            if i == 0:
                rev_str = int(rev_str)
                if orig_num < 0:
                    rev_str *= -1
    else:
        rev_str = int(orig_num)
        
    print(rev_str)

                
      
rev_int(-120)
rev_int(123)
rev_int(156)
rev_int(0)
