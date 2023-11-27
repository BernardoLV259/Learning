alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

cipher = ""
length_alphabet = len(alphabet)
for letter in range(len(text)):
    
    for a_z in range(length_alphabet):
        
        if alphabet[a_z] == text[letter]:
            a_z += shift
            if a_z > (length_alphabet - 1):
                a_z = (a_z % 25) - 1
                
            cipher = cipher + alphabet[a_z]

print(f"The encoded text is: {cipher}")

             