from Binary import Binary


def encode(text, codebook):
    encoded_message = Binary()

    for char in text:
        for binn in codebook[char]:
            encoded_message.append(binn)
    padded_bits = encoded_message.number_of_bits % 8
    for _ in range(8 - padded_bits):
        encoded_message.append(1)
    encoded_message.append_byte(padded_bits)
    return encoded_message.get_bytes()


def decode(message, codebook):
    message_bin = Binary()
    message_bin.set_bytes(message)
    message_bin.pop()
    padded_bits = message_bin.pop_byte()
    for _ in range(8 - padded_bits):
        message_bin.remove_bit()

    temp = []
    decoded_text = ""
    while message_bin.can_pop():
        temp.append(message_bin.pop())
        if temp in codebook.values():
            decoded_text += list(codebook.keys())[list(codebook.values()).index(temp)]
            temp = []

    return decoded_text
