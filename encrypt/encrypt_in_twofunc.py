abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
order= input("order 'encode' to encrypt, 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(inputed_text, shift_amount):
    cipher_text=""
    for letter in inputed_text:
        position=abc.index(letter)
        new_position=position+shift_amount
        cipher_text+=abc[new_position]
    print(f"the encoded text is {cipher_text}")

def decrypt(inputed_text, shift_amount):
    decipher_text=""
    for letter in inputed_text:
        position=abc.index(letter)
        new_position=position-shift_amount
        decipher_text+=abc[new_position]
    print(f"decoded text is {decipher_text}")
if order=="encode":
    encrypt(inputed_text=text, shift_amount=shift)
elif order=="decode":
    decrypt(inputed_text=text, shift_amount=shift)
