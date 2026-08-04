alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#            0    1    2    3    4    5
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""

    for letter in original_text:
        alphabet_index = alphabet.index(letter)
        shift_index = alphabet_index + shift_amount
        shift_index = shift_index % len(alphabet)
        encrypted_text = encrypted_text + alphabet[shift_index]

    print(f"Here is the encoded result: {encrypted_text}")

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
def decrypt(original_text, shift_amount):
    decrypted_text  = ""

    for letter in original_text:
        alphabet_index = alphabet.index(letter)
        shift_index = alphabet_index - shift_amount
        if shift_index < 0:
            shift_index = (shift_index % len(alphabet)) - len(alphabet)
        else:
            shift_index = shift_index % len(alphabet)

        decrypted_text = decrypted_text + alphabet[shift_index]

    print(f"Here is the decoded result: {decrypted_text}")


# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar():
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Please rerun and enter between 'encode' & 'decode' only!!")

caesar()