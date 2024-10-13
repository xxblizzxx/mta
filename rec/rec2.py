class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    
    new_head = head.next
    head.next = swap_pairs(new_head.next)
    new_head.next = head
    return new_head

# Допоміжна функція для створення списку з масиву
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Допоміжна функція для перетворення списку на масив
def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Приклад використання
head = create_linked_list([1, 2, 3, 4])
swapped_head = swap_pairs(head)
print(linked_list_to_array(swapped_head))  # Виведе: [2, 1, 4, 3]
