class MinStack:

    def __init__(self):
        # Ініціалізуємо основний стек і стек для мінімальних значень
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Додаємо елемент в основний стек
        self.stack.append(val)
        # Якщо мінімальний стек порожній або val <= мінімальне значення, додаємо в мінімальний стек
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Видаляємо верхній елемент з основного стека
        if self.stack:
            top = self.stack.pop()
            # Якщо верхній елемент був мінімальним, видаляємо його і з мінімального стека
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Повертаємо верхній елемент з основного стека
        if self.stack:
            return self.stack[-1]
        return None  # Випадок, коли стек порожній

    def getMin(self) -> int:
        # Повертаємо верхній елемент з мінімального стека (мінімальне значення)
        if self.min_stack:
            return self.min_stack[-1]
        return None  # Випадок, коли стек порожній
