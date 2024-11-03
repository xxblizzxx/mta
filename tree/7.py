class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # Стани вузлів:
        # 0 -> вузол не покритий
        # 1 -> вузол покритий без камери
        # 2 -> вузол покритий камерою

        self.cameras = 0

        def dfs(node):
            if not node:
                return 1  # Порожні вузли вважаються покритими
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                # Якщо хоча б один із нащадків не покритий, встановлюємо камеру
                self.cameras += 1
                return 2

            if left == 2 or right == 2:
                # Якщо хоча б один із нащадків має камеру, цей вузол покритий
                return 1

            # Вузол не покритий, але нащадки покриті
            return 0

        # Якщо корінь не покритий, додаємо камеру
        if dfs(root) == 0:
            self.cameras += 1

        return self.cameras
