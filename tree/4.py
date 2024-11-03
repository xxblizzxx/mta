# Визначаємо клас вузла дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root: TreeNode, k: int) -> int:
    # Локальна змінна для збереження результату і рахунку
    count = 0
    result = None

    def in_order(node):
        nonlocal count, result
        if not node or result is not None:
            return

        # Відвідуємо ліве піддерево
        in_order(node.left)

        # Збільшуємо лічильник і перевіряємо, чи знайшли k-й елемент
        count += 1
        if count == k:
            result = node.val
            return

        # Відвідуємо праве піддерево
        in_order(node.right)

    # Виконуємо in-order обхід
    in_order(root)
    return result
