line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
print(f"    A     B     C")
print(f"1 {line1}\n2 {line2}\n3 {line3}")
position = input("Pick 1 letter and then 1 number: Example B3\n> ") 

letter = position[0].lower() 
abc = ["a","b","c"] 

index_letter = abc.index(letter) 
index_number = int(position[1])-1

if index_number > 2:
    print("\nPlease Select one letter (A)(B)(C) and one number (1)(2)(3)\n")

else: 
    map[index_number] [index_letter] = "X"

    print(f"\n{line1}\n{line2}\n{line3}\n")
    print("X MARKED THE SPOT")