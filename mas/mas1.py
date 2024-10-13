def find_max_consecutive_ones(nums, i=0, current_count=0, max_count=0):
    if i == len(nums):  # Якщо досягли кінця масиву
        return max(current_count, max_count)
    
    if nums[i] == 1:  # Якщо зустріли 1, збільшуємо поточний лічильник
        return find_max_consecutive_ones(nums, i + 1, current_count + 1, max_count)
    else:  # Якщо зустріли 0, оновлюємо максимальне значення та обнуляємо поточний лічильник
        return find_max_consecutive_ones(nums, i + 1, 0, max(max_count, current_count))

# Приклад використання
nums1 = [1, 1, 0, 1, 1, 1]
nums2 = [1, 0, 1, 1, 0, 1]

print(find_max_consecutive_ones(nums1))  # Виведе: 3
print(find_max_consecutive_ones(nums2))  # Виведе: 2
