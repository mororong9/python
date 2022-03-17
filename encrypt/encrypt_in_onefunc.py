abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
order= input("1,encode to encrypt\n2,decode to decrypt\n select:\n")
text = input("your message:\n").lower()
shift = int(input("shift number:\n"))

def en_decrypt(inputed_text1,shift_amount1,inputed_order1):
    result_text=""
    for letter in inputed_text1:
        position=abc.index(letter)
        if inputed_order1=="1":
            new_position=position+shift_amount1
            result_text += abc[new_position]
        else:
            new_position=position-shift_amount1
            result_text+=abc[new_position]
    print(f"the encoded text is {result_text}")
en_decrypt(inputed_text1=text, shift_amount1=shift, inputed_order1=order)

