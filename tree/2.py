# Визначаємо клас вузла дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root: TreeNode) -> bool:
    def is_mirror(left: TreeNode, right: TreeNode) -> bool:
        # Якщо обидва вузли порожні, вони дзеркальні
        if not left and not right:
            return True
        # Якщо тільки один з вузлів порожній або значення різні, не дзеркальні
        if not left or not right or left.val != right.val:
            return False
        # Перевіряємо дзеркальність піддерев
        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    # Перевіряємо симетричність відносно кореня
    return is_mirror(root.left, root.right) if root else True
