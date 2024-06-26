from math import ceil


class Binary:
    def __init__(self):
        self.value = 0
        self.number_of_bits = 0

    def append(self, bit):
        self.number_of_bits += 1
        self.value = self.value << 1
        self.set(0, bit)

    def append_byte(self, byte):
        self.number_of_bits += 8
        self.value = self.value * 256
        self.value += byte

    def pop_byte(self):
        print(self.get_string())
        byte = self.value % 256
        self.value = self.value >> 8
        self.number_of_bits -= 8
        print(self.get_string())
        return byte

    def pop(self):
        output = self.get_bit_at_index(self.number_of_bits)
        self.number_of_bits -= 1
        return output

    def remove_bit(self):
        self.value = self.value >> 1
        self.number_of_bits -= 1
        return

    def can_pop(self):
        return self.number_of_bits >= 0

    def set(self, index, bit):
        if bit == 0 or bit == '0':
            self.value = self.value & ~(1 << index)
        else:
            self.value = self.value | 1 << index

    def get_bit_at_index(self, index):
        return (self.value >> index) & 1

    def set_bytes(self, bytes):
        self.number_of_bits = len(bytes) * 8
        self.value = int.from_bytes(bytes, byteorder='big')

    def get_bytes(self):
        return self.value.to_bytes(ceil(self.number_of_bits / 8), byteorder='big')

    def get_string(self):
        tab = ['0', '1']
        output = ""
        for i in range(self.number_of_bits, -1, -1):
            output += tab[self.get_bit_at_index(i)]
        return output

    def __eq__(self, other):
        if self.value == other.value:
            return True
        return False
