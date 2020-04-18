def rev_int(numb):
    digit_array = []

    for i in str(numb):
        mag_10 = len(str(numb))
        divide_numb = 10 ** (mag_10 - 1)
        
        digit = numb // divide_numb
        
        numb = numb - (int(i) * divide_numb)
        
        digit_array.append(str(digit))

    rev_numb = ''.join(digit_array)[::-1]

    print(int(rev_numb))

    return rev_numb



rev_int(1234567)
