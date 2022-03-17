
def en_decrypt(inputed_text1,shift_amount1,inputed_order1):
    result_text=""
    for letter in inputed_text1:
        if letter in abc:
            position=abc.index(letter)
            if inputed_order1=="1":
                new_position=position+shift_amount1
                result_text += abc[new_position]
            else:
                new_position=position-shift_amount1
                result_text+=abc[new_position]
        else:
            print("worng choice")
    print(f"the encoded text is : {result_text}\n")

stop = '1'

while stop=='1':
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    order = input("1,encode to encrypt\n2,decode to decrypt\n select:\n")
    text = input("your message:\n").lower()
    shift = int(input("shift number:\n"))
    shift = shift % 26

    en_decrypt(inputed_text1=text, shift_amount1=shift, inputed_order1=order)
    stop = input("1, more encrypt and decrypt\n2, stop\nselect:\n")
if stop=='2':
    print("okey bye\n")
