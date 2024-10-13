def replace_elements(arr):
    max_right = -1  # Ініціалізуємо змінну для зберігання найбільшого елемента праворуч
    
    # Пройдемо по масиву з кінця до початку
    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]  # Збережемо поточне значення елемента
        arr[i] = max_right  # Замінимо поточний елемент найбільшим елементом праворуч
        max_right = max(max_right, temp)  # Оновимо максимальний елемент праворуч
    
    return arr

# Приклад використання
arr1 = [17, 18, 5, 4, 6, 1]
print(replace_elements(arr1))  # Виведе: [18, 6, 6, 6, 1, -1]

arr2 = [400]
print(replace_elements(arr2))  # Виведе: [-1]
