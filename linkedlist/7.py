import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    # Створюємо мін-купу
    min_heap = []
    
    # Додаємо всі голови списків в мін-купу
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))

    # Створюємо фіктивний вузол для результату
    dummy = ListNode()
    current = dummy

    # Поки мін-купа не порожня
    while min_heap:
        # Дістаємо вузол з найменшим значенням
        val, i, node = heapq.heappop(min_heap)
        # Додаємо цей вузол до результатного списку
        current.next = node
        current = current.next
        # Якщо є наступний вузол у цьому списку, додаємо його до мін-купи
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next

# Функція для виводу списку для тестування
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Приклад використання
# Створюємо кілька відсортованих списків
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

# Об'єднуємо всі списки
merged_list = merge_k_lists([list1, list2, list3])

# Виводимо результат
print_list(merged_list)
