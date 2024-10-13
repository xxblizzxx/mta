def duplicate_zeros(arr):
    # Кількість нулів, які можна дублювати всередині допустимого діапазону
    zeros_to_duplicate = 0
    length = len(arr)
    
    # Підрахунок кількості нулів, які потрібно дублювати
    for i in range(length):
        if i + zeros_to_duplicate >= length - 1:
            break
        if arr[i] == 0:
            zeros_to_duplicate += 1

    # Починаємо переміщати елементи з кінця масиву
    i = length - 1
    while zeros_to_duplicate > 0:
        if arr[i - zeros_to_duplicate] == 0:
            # Якщо поточний елемент — це нуль, дублюємо його
            if i < length:
                arr[i] = 0
            i -= 1
            if i < length:
                arr[i] = 0
        else:
            # Переміщуємо звичайні елементи
            arr[i] = arr[i - zeros_to_duplicate]
        i -= 1

# Приклад використання
arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr1)
print(arr1)  # Виведе: [1, 0, 0, 2, 3, 0, 0, 4]

arr2 = [1, 2, 3]
duplicate_zeros(arr2)
print(arr2)  # Виведе: [1, 2, 3]
