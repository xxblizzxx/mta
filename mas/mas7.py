def check_if_exist(arr):
    seen = set()  # Множина для збереження елементів
    
    for num in arr:
        # Перевіряємо умови: чи є подвійний або половинний елемент у множині
        if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        # Додаємо поточний елемент до множини
        seen.add(num)
    
    return False

# Приклад використання
arr1 = [10, 2, 5, 3]
print(check_if_exist(arr1))  # Виведе: True

arr2 = [3, 1, 7, 11]
print(check_if_exist(arr2))  # Виведе: False
