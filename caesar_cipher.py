def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - base + shift) % 26 if mode == 'encrypt' else (ord(char) - base - shift) % 26
            result += chr(base + offset)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    mode = input("Encrypt or Decrypt? (e/d): ").lower()

    if mode == 'e':
        print("Encrypted:", caesar_cipher(message, shift, 'encrypt'))
    elif mode == 'd':
        print("Decrypted:", caesar_cipher(message, shift, 'decrypt'))
    else:
        print("Invalid mode selected.")