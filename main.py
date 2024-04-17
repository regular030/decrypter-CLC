import os
import string
import random
import hashlib


def clear_screen():
  # Clear screen depending on the operating system
  os.system('cls' if os.name == 'nt' else 'clear')


def hash_text(text):
  # Hash the text using SHA-256
  hash_object = hashlib.sha256(text.encode())
  return hash_object.hexdigest()


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


def homebrew_cipher(text):
  encrypted_text = ""
  for i, char in enumerate(text):
    encrypted_text += char + random.choices(string.ascii_letters, k=1)[0]
  return encrypted_text


def homebrew_decipher(text):
  decrypted_text = ""
  i = 0
  while i < len(text):
    decrypted_text += text[i]
    i += 2  # Skip the index added during encryption
  return decrypted_text


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
      print("4: Homebrew")
      cipher_choice = input("Enter your choice: ")

      clear_screen()

      if cipher_choice == '1':
        encrypted_text = reverse_cipher(text)
        print("Encrypted text:", encrypted_text)

      elif cipher_choice == '2':
        shift = int(input("Enter the shift for the Caesar cipher (0-25): "))
        encrypted_text = caesar_cipher(text, shift)
        print("Encrypted text:", encrypted_text)
        print("Decryption key:", shift)

      elif cipher_choice == '3':
        encrypted_text = atbash_cipher(text)
        print("Encrypted text:", encrypted_text)

      elif cipher_choice == '4':
        encrypted_text = homebrew_cipher(text)
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
      print("4: Homebrew")
      cipher_choice = input("Enter your choice: ")

      clear_screen()

      if cipher_choice == '1':
        decrypted_text = reverse_cipher(text)
        print("Decrypted text:", decrypted_text)

      elif cipher_choice == '2':
        shift = int(input("Enter the shift for the Caesar cipher (0-25): "))
        decrypted_text = caesar_cipher(text, shift)
        print("Decrypted text:", decrypted_text)

      elif cipher_choice == '3':
        decrypted_text = atbash_cipher(text)
        print("Decrypted text:", decrypted_text)

      elif cipher_choice == '4':
        decrypted_text = homebrew_decipher(text)
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
