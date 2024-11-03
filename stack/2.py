# Визначаємо структуру вузла бінарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Функція для виконання обходу Inorder Traversal
def inorder_traversal(root):
    result = []
    inorder_helper(root, result)
    return result

# Рекурсивна допоміжна функція для обходу
def inorder_helper(node, result):
    if node:
        inorder_helper(node.left, result)   # Відвідуємо ліве піддерево
        result.append(node.val)             # Відвідуємо поточний вузол
        inorder_helper(node.right, result)  # Відвідуємо праве піддерево

# Приклад використання
# Створюємо бінарне дерево: 1 -> null -> 2 -> 3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Виконуємо обхід
print(inorder_traversal(root))  # Output: [1, 3, 2]
