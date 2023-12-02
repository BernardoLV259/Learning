def parity_bit(*args):
    list = []

    for i in args:
        
        if i == True:
            #print(i)
            list.append(i)
    #print(list)
    if ((len(list)) % 2) == 0:
        return True
    
    else:
        return False

