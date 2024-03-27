from TreeNode import TreeNode


class TreeGenerator:
    char_dict = {}

    def __init__(self):
        self.node = None
        self.text = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

    def count_chars(self):
        for char in self.text:
            if char in self.char_dict.keys():
                self.char_dict[char] += 1
            else:
                self.char_dict[char] = 1

    def generate_tree(self):
        nodes = []
        for char in self.char_dict:
            nodes.append(TreeNode(char, self.char_dict[char]))
        for node in nodes:
            print(node, node.char)
        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.value)
            nodes.append(TreeNode('', nodes[0].value + nodes[1].value, nodes[0], nodes[1]))
            nodes.remove(nodes[0])
            nodes.remove(nodes[0])

        self.node = nodes[0]

    def get_navigation_path(self, char):
        path = ""
        node = self.node
        while node.char != char:
            if node.left.has_char(char):
                path += "0"
                node = node.left
            elif node.right.has_char(char):
                path += "1"
                node = node.right

        return path


tr = TreeGenerator()
tr.count_chars()

tr.generate_tree()

encoded_chars = {}

for char in tr.text:
    if char not in encoded_chars.keys():
        encoded_chars[char] = tr.get_navigation_path(char)

values = list(encoded_chars.values())
values.sort()
print(values)
