class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(node):
    # Копіюємо значення з наступного вузла в поточний вузол
    node.val = node.next.val
    # Змінюємо посилання поточного вузла на наступний після наступного
    node.next = node.next.next

# Функція для виводу списку для тестування
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Приклад використання
# Створимо список: 4 -> 5 -> 1 -> 9
head = ListNode(4)
node_to_delete = ListNode(5)
head.next = node_to_delete
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

# Видаляємо вузол зі значенням 5
delete_node(node_to_delete)

# Виводимо результат
print_list(head)
