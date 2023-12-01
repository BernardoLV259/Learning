def is_palist(items):
    if (len(items)) == 0:
        return True
    
    elif (len(items)) == 1:
        return True
    
    else: #list is [aba]
        #palindrome = True
        for i in items:
            
            switched = i[::-1]
            #print(f"Hello this is: {switched} and this is {i}")
            if switched != i:
                # print(switched)
                # print(i)
                return False
            
        return True


def is_file_empty(filename):
    try:
        with open(filename) as f:
            # read the file into a string
            s = f.read()

            if s == '':
                return True
            else:
                return False
            
    except FileNotFoundError:
        return None

#print(is_file_empty("not_empty.txt"))






def flat_purge(purging):
    #print(len(purging))
    purged = []
    for items in purging:
        #print(items)
        if items == []:
                purged.append('_')

        for each in items:
            #print(each)
                purged.append(each)
    
    return purged


