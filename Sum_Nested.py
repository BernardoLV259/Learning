

def count_lines(file):
    
    with open(file) as f:
        x = len(f.readlines())
        return x
        




with open("test_file_1.txt", "w") as test_file:
    test_file.writelines(['abc\n', 'def\n', 'ghi\n'])

#print(count_lines("test_file_1.txt")) # 3




def sum_nested(list):
    try:
        sum = 0
        for i in list:
            if i != int:
                pass
            else:
                sum += i
        
        return sum

    except:
        pass


