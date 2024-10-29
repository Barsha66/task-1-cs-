def caesar_cipher(text, shift, encrypt=True):
    if not encrypt:
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')    #base ASCII value depending on whether the character is uppercase or lowercase
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher Program")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'E':
        encrypted_message = caesar_cipher(message, shift, encrypt=True)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = caesar_cipher(message, shift, encrypt=False)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
