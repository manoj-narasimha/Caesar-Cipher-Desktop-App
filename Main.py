from logo import Logo #Importing the logo from logo.py
print(Logo) #Printing the logo at first.

# Alphabets from a-z
# We are adding alphabets twice just to avoid index error
# For eg: if we type 'zulu' to encode then it will look for index of z and shifts it by it's
# shift value greater than 1. We will get an index if we not add a-z twice in the list.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Defining Caesar method at first.
def Caesar(text_msg, shift_value, dir):
    """ Encode or Decode your text_message """

    end_text = ""
    if direction == "decode":
        shift_value *= -1 # Shift value becomes negative if we want to decode a text.

    for char in text_msg: # Loop through each character in text msg
        if char in alphabet:
          position = alphabet.index(char) # Find the position of each char in text msg
          new_position = position + shift_value # Adding position of char to shift value which gives new position index.
          new_char = alphabet[new_position]  # gives new position index.
          end_text += new_char
        else:
            end_text += char # If it is a space or symbol.

    print(f'The {dir}d Text is {end_text}.') # Final encoded or decoded text.


is_continue = True
while is_continue: # True
    direction = input("Enter 'Encode' or 'Decode': \n")
    msg = input("Enter the Text: \n").lower()
    shift = int(input("Enter the shift amount: \n"))
    if shift > 51:
        shift = shift % 26

    Caesar(text_msg=msg, shift_value=shift, dir=direction)
    result = input("Do you want to continue (Y/N): ")

    if result == "N" or result == "NO": # False
        is_continue = False
        print("Good Bye!!!") # Loop ends here.
    elif result == "Y" or result == "YES":
        is_continue = True # Loop continues here.
   