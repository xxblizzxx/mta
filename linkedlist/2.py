class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head):
    current = head

    # Проходимо по списку, видаляючи дублікати
    while current and current.next:
        if current.val == current.next.val:
            # Пропускаємо дубльований вузол
            current.next = current.next.next
        else:
            # Переходимо до наступного вузла
            current = current.next

    return head

# Функція для виводу списку для тестування
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Приклад використання
# Створюємо відсортований список з дублікатами: 1 -> 1 -> 2 -> 3 -> 3
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

# Видаляємо дублікати
unique_list = delete_duplicates(head)

# Виводимо результат
print_list(unique_list)
