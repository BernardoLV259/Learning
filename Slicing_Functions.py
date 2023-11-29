
def parity_bit(*bool):
    list = []
    for i in range(len(bool)):
        if bool[i] == True:
            list.append(bool[i])
    
    if ((len(list)) % 2) == 0:
        return True
    else:
        return False


def first_last(input):
    
    
    if (len(input)) == 0:
        return None
    else:
        list = []
        list.append(input[0])
        list.append(input[-1])
        tuple_made = tuple(list)
        return tuple_made




