class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = head
    fast = head

    # Рухаємо повільний та швидкий вказівники
    while fast and fast.next:
        slow = slow.next          # повільний вказівник рухається на 1 вузол
        fast = fast.next.next      # швидкий вказівник рухається на 2 вузли

        # Якщо повільний та швидкий вказівники зустрілися, значить є цикл
        if slow == fast:
            return True

    # Якщо дійшли до кінця списку, циклу немає
    return False

# Приклад використання
# Створюємо список з циклом: 3 -> 2 -> 0 -> -4, де -4 вказує на вузол з індексом 1 (тобто на вузол зі значенням 2)
head = ListNode(3)
second = ListNode(2)
third = ListNode(0)
fourth = ListNode(-4)

# Формуємо зв'язки
head.next = second
second.next = third
third.next = fourth
fourth.next = second  # Це створює цикл, де останній вузол вказує на вузол з індексом 1

# Перевіряємо на наявність циклу
print(has_cycle(head))  # Виведе True
