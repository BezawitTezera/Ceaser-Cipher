alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

text_list = list(text)
index = alphabet.index(text_list[0])
encrypted_list = []
decrypted_list = []

def encrypt(texts, shifts, start_index):
    for value in text_list:
        encrypted_list.append(alphabet[alphabet.index(value) + shifts])
    return "".join(encrypted_list)

def decrypt(texts, shifts, start_index):
    for value in text_list:
        decrypted_list.append(alphabet[alphabet.index(value) - shifts])
    return "".join(decrypted_list)

if direction == "encode":
    print(encrypt(text, shift, index))
elif direction == "decode":
    print(decrypt(text, shift, index))
else:
    print("Enter a valid input.")




