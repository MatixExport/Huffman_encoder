class TreeNode:

    def __init__(self, char='', value=0, left=None, right=None):
        self.char = char
        self.value = value
        self.left = left
        self.right = right

    def has_char(self, char):
        if self.char == char:
            return True
        if self.left is not None:
            if self.left.has_char(char):
                return True
        if self.right is not None:
            return self.right.has_char(char)
        return False
