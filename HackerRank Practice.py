def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        if ((i%5) == 0) and ((i%3)==0):
            print("FizzBuzz")
            
        elif (i%5) == 0:
            print("Buzz")
        
        elif (i%3)==0:
            print("Fizz")
        else:
            print(i)









jump = 1

def jumps(flagHeight, bigJump):
    # Write your code here
    remainder = flagHeight % bigJump #2
    floor = flagHeight // bigJump
    amount = remainder + floor
    
    return amount
