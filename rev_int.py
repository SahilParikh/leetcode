def rev_int(x):
    '''
    Given a 32-bit signed integer, reverse digits of an integer
    
    x = singed 32 bit int
    '''
    orig_num = x
    x = str(abs(x)).rstrip('0')
    rev_str = ''
    
    for i in range(len(x)-1,-1,-1):
        rev_str += x[i]
        if i == 0:
            rev_str = int(rev_str)
            if rev_str / (-1 * rev_str) != orig_num / (-1 * orig_num) :
                rev_str *= -1
     return(rev_str)

                
      
rev_int(-120)
rev_int(-334)
rev_int(156)
