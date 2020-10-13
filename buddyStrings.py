a = input("Enter a str: " )
b = input("Enter a another str: ")

def buddyStrings(a, b):
    res = []
    aCopy = []
    if len(a) == len(b) and a != b:
        for i in range(len(a)):
            aCopy.append(a[i])
            if a[i] != b[i]:
                res.append(i)
                
        if len(res) == 2:
            aCopy[res[0]] = b[res[0]]
            aCopy[res[1]] = b[res[1]]

            if ''.join(aCopy) == b:
                print('True')
        else:
            print('False')
    else:
        print('False')

                
buddyStrings(a,b)
