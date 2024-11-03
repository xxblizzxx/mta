class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if not head or not head.next:
        return

    # Крок 1: Знайдемо середину списку
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Крок 2: Розділимо список на дві частини і розвернемо другу частину
    second = slow.next
    slow.next = None  # Закінчуємо першу частину списку
    prev = None
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    second = prev  # Тепер друга частина є перевернутою

    # Крок 3: Почергово з'єднуємо вузли з обох частин
    first, second = head, second
    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

# Функція для виводу списку для тестування
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Приклад використання
# Створюємо список: 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# Перепорядковуємо список
reorder_list(head)

# Виводимо результат
print_list(head)
