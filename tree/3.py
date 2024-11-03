# Визначаємо клас вузла дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: TreeNode) -> TreeNode:
    # Якщо вузол порожній, повертаємо None
    if root is None:
        return None
    
    # Рекурсивно інвертуємо ліве і праве піддерева
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    
    # Повертаємо корінь після інверсії
    return root
