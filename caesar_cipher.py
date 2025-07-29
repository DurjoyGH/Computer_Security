def encrypt(text, shift):
    result = ""
    
    for char in text:
        if(char.isupper()):
            result += chr((ord(char) - 65) % 26 + 65 + shift)
             
        elif char.islower():
            result += chr((ord(char) - 97) % 26 + 97 + shift)
            
        else:
            result += char
            
    return result


def decrypt(cipher, shift):
    return encrypt(cipher, -shift)

message = input("Enter the secret message: ")
shift_value = int(input("Enter the shift value: "))

plain_text = message
shift = shift_value

encrypted_text = encrypt(plain_text, shift)
decrypted_text = decrypt(encrypted_text, shift)


print("Plain Text: ", plain_text)

print("Encrypted Text: ", encrypted_text)

print("Decrypted Text: ", decrypted_text)