def sort_array_by_parity(nums):
    evens = []  # Список для парних чисел
    odds = []   # Список для непарних чисел
    
    # Проходимо по масиву і розподіляємо елементи
    for num in nums:
        if num % 2 == 0:
            evens.append(num)  # Додаємо до списку парних
        else:
            odds.append(num)   # Додаємо до списку непарних
    
    return evens + odds  # Об'єднуємо парні та непарні числа

# Приклад використання
nums1 = [3, 1, 2, 4]
print(sort_array_by_parity(nums1))  # Виведе: [2, 4, 3, 1] або інший допустимий варіант

nums2 = [0]
print(sort_array_by_parity(nums2))  # Виведе: [0]
