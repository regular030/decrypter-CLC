import os
import string


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


def main():
  clear_screen()

  while True:
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option: ")

    clear_screen()

    text = input("Enter the text you want to process (type 'exit' to quit): ")
    if text.lower() == 'exit':
      break

    clear_screen()

    if choice == '1':
      cipher_choice = input(
          "Choose a cipher (1: Reverse, 2: Caesar, 3: Atbash): ")

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
      cipher_choice = input(
          "Choose a cipher (1: Reverse, 2: Caesar, 3: Atbash): ")

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

    else:
      print("Invalid option")

    input("\nPress Enter to continue...")
    clear_screen()


if __name__ == "__main__":
  main()
