from Binary import Binary
from TreeNode import TreeNode


class TreeGenerator:
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'w',
             'x', 'y', 'z', ' ']
    char_count = [0 for i in chars]

    def encode(self, char_message_dir):
        to_send = Binary()
        to_send.pop()  # usuwamy początkowe 0

        for char in self.text:
            for binn in char_message_dir[char]:
                to_send.append(binn)
        return to_send

    def decode(self, message, char_message_dir):
        temp = []
        decoded_text = ""
        while message.can_pop():
            temp.append(message.pop())
            if temp in char_message_dir.values():
                decoded_text += list(char_message_dir.keys())[list(char_message_dir.values()).index(temp)]
                temp = []

        return decoded_text

    def __init__(self):
        self.nodes = []
        self.text = "ala ma kotasdfsdafe asdfsdifgj mkdfg pdfugnadf nihs e prfjn aesf a sergdsgbccqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"

    def count_chars(self):
        for i in range(len(self.chars)):
            self.char_count[i] = self.text.count(self.chars[i])

    def generate_tree(self):
        for char, count in zip(self.chars, self.char_count):
            if count > 0:
                self.nodes.append(TreeNode(char, count))

        while len(self.nodes) > 1:
            self.nodes.sort(key=lambda x: x.value)
            self.nodes.append(TreeNode('', self.nodes[0].value + self.nodes[1].value, self.nodes[0], self.nodes[1]))
            self.nodes.remove(self.nodes[0])
            self.nodes.remove(self.nodes[0])

    def get_navigation_path(self, char):
        path = ""
        node = self.nodes[0]
        while node.char != char:
            if node.left.has_char(char):
                path += "0"
                node = node.left
            elif node.right.has_char(char):
                path += "1"
                node = node.right
            else:
                break

        return path

    def get_char_lengths(self):
        char_length = {}
        for char in self.chars:
            char_length[char] = len(self.get_navigation_path(char))

        return char_length.values()

    def group_chars_by_lengths(self):
        lengths = [[] for _ in range(8)]

        for char in self.chars:
            lengths[len(self.get_navigation_path(char))].append(char)
        return lengths

    def get_codebook(self, lengths):
        char_message_dir = {}

        message = []
        for i in range(len(lengths)):
            for element in lengths[i]:
                for j in range(len(message) - 1, -1, -1):
                    if message[j] == 1:
                        message[j] = 0
                    else:
                        message[j] += 1
                        break

                while len(message) < i:
                    message.append(0)

                char_message_dir[element] = message.copy()

        return char_message_dir


tr = TreeGenerator()
tr.count_chars()
tr.generate_tree()
print(
    tr.decode(
        tr.encode(
            tr.get_codebook(
                tr.group_chars_by_lengths()
            )
        ),
        tr.get_codebook(tr.group_chars_by_lengths())
    ))
