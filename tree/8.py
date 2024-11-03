from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root: TreeNode):
    # Словник для зберігання вузлів за стовпцями
    node_map = defaultdict(list)

    # Черга для BFS з координатами (вузол, рядок, стовпець)
    queue = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()
        if node:
            # Додаємо вузол до словника з координатами
            node_map[col].append((row, node.val))
            # Додаємо лівий і правий вузли до черги з оновленими координатами
            queue.append((node.left, row + 1, col - 1))
            queue.append((node.right, row + 1, col + 1))

    # Сортуємо стовпці та вузли всередині кожного стовпця
    result = []
    for col in sorted(node_map.keys()):
        # Сортуємо вузли: спочатку за рядком, потім за значенням
        column_nodes = sorted(node_map[col], key=lambda x: (x[0], x[1]))
        result.append([val for row, val in column_nodes])

    return result
