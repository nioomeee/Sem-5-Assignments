# Create a program that uses the with statement to encrypt and decrypt a text file
# using a simple cipher. Handle errors if the file is missing or unreadable.
import string 

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

        self.alphabet = string.ascii_lowercase

        self.shifted_alphabet = self.alphabet[shift:] + self.alphabet[:shift]

        print(f"\n Normal alphabet: {self.alphabet}\n Shifted alphabet: {self.shifted_alphabet}")

    def _transform(self, text, from_alphabet, to_alphabet):
        transformed_text=""
        for char in text:
            lower_char = char.lower()
            if lower_char in from_alphabet:
                index = from_alphabet.find(lower_char)
                new_char = to_alphabet[index]
                transformed_text += new_char.upper() if char.isupper() else new_char
            else:
                transformed_text += char

        return transformed_text
    
    def encrypt(self, text):
        return self._transform(text, self.alphabet, self.shifted_alphabet)
    
    def decrypt(self, text):
        return self._transform(text, self.shifted_alphabet, self.alphabet)
    
def processFile(cipher_action, input_filename, output_filename):
    try:
        with open(input_filename, "r") as infile, open(output_filename, "w") as outfile:
            print(f"\n Reading from '{input_filename}'...")
            content = infile.read()

            print("\n Processing content ...")
            transformed_text = cipher_action(content)

            outfile.write(transformed_text)
            print(f"\n Successfully wrote to '{output_filename}'")

    except FileNotFoundError:
        print(f"\n Error! {input_filename} not found")
    except Exception as e:
        print(f"\n An exception occured: {e}")

my_cipher = CaesarCipher(5)

print("\n ---- Encrypting File ----")
processFile(my_cipher.encrypt, "secret.txt", "encrypted.txt")

print("\n ---- Decrypting File ----")
processFile(my_cipher.decrypt, "encrypted.txt", "decrypted.txt")

print("\n ---- Testing Error handling ----")
processFile(my_cipher.encrypt, "nofile.txt", "output.txt")