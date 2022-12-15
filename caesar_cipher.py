alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(combined_text, shift_amount, in_direction):
  final_text = ""
  for letter in combined_text:
    position = alphabet.index(letter)
    if in_direction == "encode":
      new_position = position + shift_amount
    elif in_direction == "decode":
      new_position = position - shift_amount
    final_text += alphabet[new_position]
  print(f"The {in_direction}d text is {final_text}")

caesar(combined_text=text, shift_amount=shift, in_direction=direction)
