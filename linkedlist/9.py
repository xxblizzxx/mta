class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    # Створюємо два списки: для вузлів менших за x і для вузлів більших або рівних x
    before_head = ListNode(0)  # Початковий вузол для вузлів < x
    after_head = ListNode(0)   # Початковий вузол для вузлів >= x

    before = before_head  # Вказівник на останній вузол в списку вузлів < x
    after = after_head    # Вказівник на останній вузол в списку вузлів >= x

    # Проходимо по всьому списку
    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    # З'єднуємо два списки
    after.next = None         # Завершуємо список вузлів >= x
    before.next = after_head.next  # Приєднуємо "after" список до кінця "before" списку

    return before_head.next

# Функція для виводу списку для тестування
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Приклад використання
# Створюємо список: 1 -> 4 -> 3 -> 2 -> 5 -> 2
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))

# Розділяємо список при x = 3
x = 3
partitioned_list = partition(head, x)

# Виводимо результат
print_list(partitioned_list)
