class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def double_linked_list_number(head):
    # Перевіримо наявність голови
    if not head:
        return None

    # Рекурсивно подвоюємо число з кінця списку
    carry = double_helper(head)

    # Якщо є перенесення, додаємо новий вузол на початку списку
    if carry:
        new_head = ListNode(carry)
        new_head.next = head
        head = new_head

    return head

def double_helper(node):
    if not node:
        return 0  # Базовий випадок: перенесення відсутнє

    # Подвоюємо наступний вузол і отримуємо перенесення
    carry = double_helper(node.next)

    # Подвоюємо поточне значення вузла з врахуванням перенесення
    total = node.val * 2 + carry
    node.val = total % 10  # Залишаємо тільки цифру в поточному вузлі
    return total // 10     # Повертаємо перенесення до наступного вузла

# Функція для виводу списку для тестування
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Приклад використання
# Створимо список: 1 -> 8 -> 9
head = ListNode(1, ListNode(8, ListNode(9)))

# Подвоїмо число
doubled_list = double_linked_list_number(head)

# Виводимо результат
print_list(doubled_list)
