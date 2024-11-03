# Визначаємо клас вузла дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root: TreeNode) -> int:
    # Ініціалізуємо змінну для зберігання глобального максимуму
    max_sum = float('-inf')

    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0

        # Рекурсивно обчислюємо максимальний шлях для лівого та правого піддерев
        left_gain = max(max_gain(node.left), 0)  # Ігноруємо негативні значення
        right_gain = max(max_gain(node.right), 0)

        # Максимальна сума шляху, що проходить через поточний вузол
        current_max_path = node.val + left_gain + right_gain

        # Оновлюємо глобальний максимум, якщо поточний шлях є кращим
        max_sum = max(max_sum, current_max_path)

        # Повертаємо максимальний шлях, що включає поточний вузол і один із його піддерев
        return node.val + max(left_gain, right_gain)

    # Викликаємо рекурсивну функцію для кореня
    max_gain(root)
    return max_sum
