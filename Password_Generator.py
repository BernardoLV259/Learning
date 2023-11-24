#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for letter in (range(1,nr_letters+1)): 
  length_letter = len(letters) 
  random_letter = random.randint(0,length_letter-1)
  password.append(letters[random_letter])

for number in (range(1,nr_numbers+1)):
  length_num = len(numbers)
  random_number = random.randint(0,length_num-1)
  password.append(numbers[random_number])

for symbol in (range(1,nr_symbols+1)):
  length_sym = len(symbols)
  random_symbol = random.randint(0,length_sym-1)
  password.append(symbols[random_symbol])

password_lenth = len(password) 
scrambled_password = []
for word in range(0,password_lenth):
  password_len = len(password) 
  random_index = random.randint(0,password_len-1)
  scrambled_password.append(password[random_index])
  del password[random_index]

NEWPASSWORD = "".join(scrambled_password)
print(f"Your New Password is: {NEWPASSWORD}")
  
