from TreeNode import TreeNode


class TreeGenerator:
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w',
             'x', 'y', 'z', ' ']
    char_count = [0 for i in chars]

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


tr = TreeGenerator()
tr.count_chars()
tr.generate_tree()
lengths = [[] for _ in range(8)]

for char in tr.chars:
    lengths[len(tr.get_navigation_path(char))].append(char)

print(lengths)
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

        str_mes = ""
        for binn in message:
            if binn == 0:
                str_mes += "0"
            else:
                str_mes += "1"
        print(str_mes)

char_length = {}
for char in tr.chars:
    char_length[char] = len(tr.get_navigation_path(char))

print(char_length.values())  # to send
