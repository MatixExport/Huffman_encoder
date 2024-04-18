from Binary import Binary


def encode(text, codebook):
    encoded_message = Binary()

    for char in text:
        for binn in codebook[char]:
            encoded_message.append(binn)
    encoded_message.pop()  # usuwamy początkowe 0
    return encoded_message.get_bytes()


def decode(message, codebook):
    temp = []
    decoded_text = ""
    message_bin = Binary()
    message_bin.set_bytes(message)
    while message_bin.can_pop():
        temp.append(message_bin.pop())
        if temp in codebook.values():
            decoded_text += list(codebook.keys())[list(codebook.values()).index(temp)]
            temp = []

    return decoded_text
