class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k      # Масив фіксованого розміру для зберігання елементів
        self.max_size = k         # Максимальний розмір черги
        self.front = -1           # Початкова позиція для початку черги
        self.rear = -1            # Початкова позиція для кінця черги
        self.size = 0             # Поточний розмір черги

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size  # Оновлення rear з круговим ефектом
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            # Якщо черга має один елемент, скидаємо front і rear
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size  # Оновлення front з круговим ефектом
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
