class MyQueue:

    def __init__(self):
        # Ініціалізуємо два стеки
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # Додаємо елемент у stack_in
        self.stack_in.append(x)

    def pop(self) -> int:
        # Переносимо елементи зі stack_in до stack_out, якщо stack_out порожній
        self._shift_stacks()
        # Видаляємо верхній елемент зі stack_out
        return self.stack_out.pop() if self.stack_out else None

    def peek(self) -> int:
        # Переносимо елементи зі stack_in до stack_out, якщо stack_out порожній
        self._shift_stacks()
        # Повертаємо верхній елемент зі stack_out
        return self.stack_out[-1] if self.stack_out else None

    def empty(self) -> bool:
        # Черга порожня, якщо обидва стеки порожні
        return not self.stack_in and not self.stack_out

    def _shift_stacks(self):
        # Переносимо елементи зі stack_in до stack_out, якщо stack_out порожній
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
