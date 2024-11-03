class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(list1, list2):
    # Створимо фіктивний вузол для зручності
    dummy = ListNode()
    current = dummy

    # Об'єднуємо обидва списки
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Додаємо залишок вузлів з одного зі списків, якщо інший уже порожній
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # Повертаємо об'єднаний список, починаючи з наступного після фіктивного вузла
    return dummy.next

# Функція для виводу списку для тестування
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Приклад використання
# Створюємо перший список: 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))
# Створюємо другий список: 1 -> 3 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Об'єднуємо списки
merged_list = merge_two_sorted_lists(list1, list2)

# Виводимо результат
print_list(merged_list)
