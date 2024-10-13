def sorted_squares(nums):
    def helper(left, right, result):
        if left > right:  # Умови завершення рекурсії
            return result
        
        # Квадрат лівого та правого елементів
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        
        # Додаємо більший квадрат в кінець результатного масиву
        if left_square > right_square:
            result[right - left] = left_square
            return helper(left + 1, right, result)
        else:
            result[right - left] = right_square
            return helper(left, right - 1, result)
    
    # Ініціалізація результатного масиву
    result = [0] * len(nums)
    return helper(0, len(nums) - 1, result)

# Приклад використання
nums1 = [-4, -1, 0, 3, 10]
nums2 = [-7, -3, 2, 3, 11]

print(sorted_squares(nums1))  # Виведе: [0, 1, 9, 16, 100]
print(sorted_squares(nums2))  # Виведе: [4, 9, 9, 49, 121]
