# Визначаємо клас вузла дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    # Якщо обидва вузли порожні, то вони однакові
    if not p and not q:
        return True
    # Якщо один із вузлів порожній або значення не співпадають
    if not p or not q or p.val != q.val:
        return False
    # Рекурсивно перевіряємо ліві і праві піддерева
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
