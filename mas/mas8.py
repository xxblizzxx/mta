def valid_mountain_array(arr):
    n = len(arr)
    
    if n < 3:
        return False  # Гірський масив повинен мати як мінімум 3 елементи
    
    # Знайдемо пік
    i = 0

    # Підйом: шукаємо, де закінчується зростання
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
    
    # Пік не може бути першим або останнім елементом
    if i == 0 or i == n - 1:
        return False

    # Спад: перевіряємо спадання
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
    
    # Якщо дійшли до кінця масиву, то це дійсний гірський масив
    return i == n - 1

# Приклад використання
arr1 = [2, 1]
print(valid_mountain_array(arr1))  # Виведе: False

arr2 = [3, 5, 5]
print(valid_mountain_array(arr2))  # Виведе: False

arr3 = [0, 3, 2, 1]
print(valid_mountain_array(arr3))  # Виведе: True
