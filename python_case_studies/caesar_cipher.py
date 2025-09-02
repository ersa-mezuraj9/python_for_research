import string

# EX 1
alphabet = " " + string.ascii_lowercase

# EX 2
positions = {char: i for i, char in enumerate(alphabet)}
print(positions['n'])

# EX 3 
positions = {char: index for index, char in enumerate(alphabet)}

message = "hi my name is caesar"

encoded_message = ""
for char in message:
    new_index = (positions[char] + 1) % 27
    encoded_message += alphabet[new_index]

print(encoded_message)

# EX 4
def encoding(message, key):
    encoded = ""
    for char in message:
        new_index = (positions[char] + key) % 27
        encoded += alphabet[new_index]
    return encoded

encoded_message = encoding(message, 3)
print(encoded_message)

# EX 5
decoded_message = encoding(encoded_message, -3)
print(decoded_message)



