import os
import string
import hashlib


def clear_screen():
  # Clear screen depending on the operating system
  os.system('cls' if os.name == 'nt' else 'clear')


def reverse_cipher(text):
  return text[::-1]


def caesar_cipher(text, shift):
  encrypted_text = ""
  for char in text:
    if char.isalpha():
      shifted_index = (string.ascii_lowercase.index(char.lower()) + shift) % 26
      if char.islower():
        encrypted_text += string.ascii_lowercase[shifted_index]
      else:
        encrypted_text += string.ascii_uppercase[shifted_index]
    else:
      encrypted_text += char
  return encrypted_text


def atbash_cipher(text):
  encrypted_text = ""
  for char in text:
    if char.isalpha():
      if char.islower():
        encrypted_text += chr(122 - ord(char) + 97)
      else:
        encrypted_text += chr(90 - ord(char) + 65)
    else:
      encrypted_text += char
  return encrypted_text


def generate_caesar_decryption_key(shift):
  return 26 - shift


def hash_text(text):
  # Hash the text using the SHA-256 algorithm
  return hashlib.sha256(text.encode()).hexdigest()


def main():
  clear_screen()

  while True:
    print("Choose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Hash")
    print("4. Exit")
    choice = input("Enter your choice: ")

    clear_screen()

    if choice == '1':
      text = input("Enter the text you want to encrypt: ")

      clear_screen()

      print("Choose a cipher:")
      print("1: Reverse")
      print("2: Caesar")
      print("3: Atbash")
      cipher_choice = input("Enter your choice: ")

      clear_screen()

      if cipher_choice == '1':
        encrypted_text = reverse_cipher(text)
        print("Encrypted text:", encrypted_text)
      elif cipher_choice == '2':
        shift = int(input("Enter the shift for the Caesar cipher (0-25): "))
        encrypted_text = caesar_cipher(text, shift)
        print("Encrypted text:", encrypted_text)
        print("Decryption key:", generate_caesar_decryption_key(shift))
      elif cipher_choice == '3':
        encrypted_text = atbash_cipher(text)
        print("Encrypted text:", encrypted_text)
      else:
        print("Invalid choice")

    elif choice == '2':
      text = input("Enter the text you want to decrypt: ")

      clear_screen()

      print("Choose a cipher:")
      print("1: Reverse")
      print("2: Caesar")
      print("3: Atbash")
      cipher_choice = input("Enter your choice: ")

      clear_screen()

      if cipher_choice == '1':
        decrypted_text = reverse_cipher(text)
        print("Decrypted text:", decrypted_text)
      elif cipher_choice == '2':
        shift = int(input("Enter the shift for the Caesar cipher (0-25): "))
        decrypted_text = caesar_cipher(text,
                                       generate_caesar_decryption_key(shift))
        print("Decrypted text:", decrypted_text)
      elif cipher_choice == '3':
        decrypted_text = atbash_cipher(text)
        print("Decrypted text:", decrypted_text)
      else:
        print("Invalid choice")

    elif choice == '3':
      text = input("Enter the text you want to hash: ")
      hashed_text = hash_text(text)
      print("Hashed text:", hashed_text)

    elif choice == '4':
      break

    else:
      print("Invalid choice")

    input("\nPress Enter to go back to main menu")
    clear_screen()


if __name__ == "__main__":
  main()
