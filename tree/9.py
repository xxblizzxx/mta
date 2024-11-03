# Визначаємо клас вузла дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        index = 0

        def parse_next():
            nonlocal index
            level = 0
            # Визначаємо рівень (глибину) вузла за кількістю тире
            while index < len(traversal) and traversal[index] == '-':
                level += 1
                index += 1
            # Збираємо числове значення вузла
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
            return level, value

        def build_tree(current_level):
            if index >= len(traversal):
                return None

            level, value = parse_next()
            if level != current_level:
                # Якщо рівень не відповідає очікуваному, повертаємося
                index -= len(str(value)) + level
                return None

            # Створюємо вузол
            node = TreeNode(value)
            # Рекурсивно створюємо ліве і праве піддерева
            node.left = build_tree(current_level + 1)
            node.right = build_tree(current_level + 1)
            return node

        return build_tree(0)
