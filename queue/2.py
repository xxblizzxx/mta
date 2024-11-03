from collections import deque

class MyStack:

    def __init__(self):
        # Ініціалізуємо дві черги
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        # Додаємо новий елемент у queue2
        self.queue2.append(x)
        
        # Переміщуємо всі елементи з queue1 в queue2
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        # Обмінюємо queue1 і queue2, тепер queue1 містить всі елементи в потрібному порядку
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        # Видаляємо та повертаємо перший елемент з queue1, який є верхівкою стека
        return self.queue1.popleft() if not self.empty() else None

    def top(self) -> int:
        # Повертаємо перший елемент з queue1 без видалення
        return self.queue1[0] if not self.empty() else None

    def empty(self) -> bool:
        # Перевіряємо, чи порожня queue1
        return len(self.queue1) == 0
