from Binary import Binary
from codebookGenerator import *


def encode(text):
    lengths = get_char_lengths(text)
    char_message_dir = generate_codebook(lengths)

    encoded_message = Binary()

    for char in text:
        for binn in char_message_dir[char]:
            encoded_message.append(binn)
    encoded_message.pop()  # usuwamy początkowe 0
    return encoded_message


def decode(message, lengths):
    char_message_dir = generate_codebook(lengths)
    temp = []
    decoded_text = ""
    while message.can_pop():
        temp.append(message.pop())
        if temp in char_message_dir.values():
            decoded_text += list(char_message_dir.keys())[list(char_message_dir.values()).index(temp)]
            temp = []

    return decoded_text


# message_to_send = encode("xddfgh").get_bytes()
# received_message = Binary()
#
# received_message.set_bytes(message_to_send)
#
# codebook_to_send = get_char_lengths("xddfgh")
# # nie mamy paddingu więc akurat nam dodaje coś na początku
#
# print(decode(received_message, codebook_to_send))
