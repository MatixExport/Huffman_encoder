from TreeNode import TreeNode


class TreeGenerator:
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w',
             'x', 'y', 'z', ' ']
    char_count = [0 for i in chars]

    def __init__(self):
        self.nodes = []
        self.text = "ala ma kota"

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

        return path


tr = TreeGenerator()
tr.count_chars()
tr.generate_tree()
for char in tr.text:
    print(tr.get_navigation_path(char))
