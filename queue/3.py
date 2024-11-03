from collections import deque

class RecentCounter:

    def __init__(self):
        # Ініціалізуємо чергу для зберігання запитів
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Додаємо новий запит до черги
        self.requests.append(t)
        
        # Видаляємо всі запити, які знаходяться поза інтервалом [t - 3000, t]
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        # Повертаємо кількість запитів у черзі, яка відповідає кількості запитів за останні 3000 мс
        return len(self.requests)
