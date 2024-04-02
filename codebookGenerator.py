from TreeNode import TreeNode

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'w',
         'x', 'y', 'z', ' ']


def generate_codebook(lengths):
    groups = group_chars_by_lengths(lengths)

    codebook = {}
    expected_message_len = 0
    message = []
    for group in groups:
        for element in group:
            message = increment_binary_table(message)

            while len(message) < expected_message_len:
                message.append(0)

            codebook[element] = message.copy()
        expected_message_len += 1

    return codebook


def get_char_lengths(text):
    main_node = generate_tree(text)
    char_length = []
    for char in chars:
        char_length.append(len(get_navigation_path(char, main_node)))

    return char_length


def generate_tree(text):
    nodes = []
    char_count = count_chars(text)
    for char, count in zip(chars, char_count):
        if count > 0:
            nodes.append(TreeNode(char, count))

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.value)
        nodes.append(TreeNode('', nodes[0].value + nodes[1].value, nodes[0], nodes[1]))
        nodes.remove(nodes[0])
        nodes.remove(nodes[0])

    return nodes[0]


def count_chars(text):
    char_count = []
    for char in chars:
        char_count.append(text.count(char))

    return char_count


def get_navigation_path(char, main_node):
    path = ""
    node = main_node
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


def group_chars_by_lengths(char_lengths):
    groups = [[] for _ in range(max(char_lengths) + 1)]

    for char_index in range(len(chars)):
        groups[char_lengths[char_index]].append(chars[char_index])
    return groups


def increment_binary_table(tab):
    for j in range(len(tab) - 1, -1, -1):
        if tab[j] == 1:
            tab[j] = 0
        else:
            tab[j] += 1
            return tab
    return tab
