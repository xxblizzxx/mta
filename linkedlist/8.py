class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    # Функція для перевертання підсписку
    def reverse(start, end):
        prev = None
        current = start
        while current != end:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    # Перевірка, чи є достатня кількість вузлів для перевертання
    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy

    while True:
        # Знаходимо кінець поточної групи
        kth = prev_group
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next

        # Зберігаємо наступний вузол після групи
        group_next = kth.next

        # Перевертаємо поточну групу
        prev, curr = group_next, prev_group.next
        while curr != group_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # З'єднуємо перевернуту групу з попередньою частиною списку
        temp = prev_group.next
        prev_group.next = kth
        prev_group = temp

# Функція для виводу списку для тестування
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Приклад використання
# Створюємо список: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Перевертаємо вузли в k-групах, де k = 2
k = 2
reversed_list = reverse_k_group(head, k)

# Виводимо результат
print_list(reversed_list)
