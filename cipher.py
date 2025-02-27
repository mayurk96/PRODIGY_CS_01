alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption (plain_text,shift_key):
    ciper_text=""
    for char in plain_text:
        if char in alpha:
            position=alpha.index(char)
            new_position=(position+shift_key)%26
            ciper_text +=alpha[new_position]
        else:
            ciper_text += char
    print(f"here is the text after encryption : {ciper_text}")

def decryption (ciper_text,shift_key):
    plain_text=""
    for char in ciper_text:
        if char in alpha:
            position=alpha.index(char)
            new_position=(position-shift_key)%26
            plain_text +=alpha[new_position]
        else :
            plain_text += char
    print(f"here is the text after encryption : {plain_text}")
wanna_end = False
while not wanna_end:
    what_to_do = input("type 'encrypt' for encryption ,type 'decrypt' for decryption")
    text = input("enter message:\n").lower()
    shift = int(input("enter shift key:\n"))
    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif what_to_do == "decrypt":
        decryption(ciper_text=text, shift_key=shift)
    play_again = input("enter 'yes' to continue ,enter 'no' to end\n")
    if play_again == 'no':
        wanna_end = True
        print("Bye!! have a good day")