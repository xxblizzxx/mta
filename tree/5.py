from collections import deque

# Визначаємо клас вузла дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Серіалізує дерево в рядок."""
        if not root:
            return "[]"

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        # Видаляємо всі "null" з кінця, щоб уникнути зайвих значень
        while result and result[-1] == "null":
            result.pop()

        return "[" + ",".join(result) + "]"

    def deserialize(self, data: str) -> TreeNode:
        """Десеріалізує рядок в бінарне дерево."""
        if data == "[]":
            return None

        values = data[1:-1].split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1

        while queue:
            node = queue.popleft()
            if index < len(values) and values[index] != "null":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1

            if index < len(values) and values[index] != "null":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1

        return root
