def count_even_digit_numbers(nums, i=0, count=0):
    if i == len(nums):  # Якщо досягли кінця масиву
        return count
    
    # Перевірка на парність кількості цифр
    if len(str(nums[i])) % 2 == 0:
        return count_even_digit_numbers(nums, i + 1, count + 1)
    else:
        return count_even_digit_numbers(nums, i + 1, count)

# Приклад використання
nums1 = [12, 345, 2, 6, 7896]
nums2 = [555, 901, 482, 1771]

print(count_even_digit_numbers(nums1))  # Виведе: 2
print(count_even_digit_numbers(nums2))  # Виведе: 1
