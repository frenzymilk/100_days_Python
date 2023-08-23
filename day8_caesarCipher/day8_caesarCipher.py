from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(text=None, shift=None, direction=None):
    converted_text = ""
    for letter in text:
        if letter not in alphabet:
            shifted_letter = letter
        else:
            original_ind = alphabet.index(letter)
            if direction == "encode":
                # if original_ind + shift < 25:
                #     shifted_letter = alphabet[original_ind + shift]
                # else:
                shifted_letter = alphabet[(original_ind + shift)%26]
            elif direction =="decode":
                shifted_letter = alphabet[(original_ind - shift)%26]
        converted_text += shifted_letter
    print(f"The transformed text is {converted_text}")


continue_caesar = True
while continue_caesar:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)
    user_continue = input("Do you want to run the algorithm again ? Type 'yes' to continue and 'no' to stop. \n")
    if user_continue == "no":
        continue_caesar = False
    elif user_continue == "yes":
        continue_caesar = True