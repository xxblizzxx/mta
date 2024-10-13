def merge(nums1, m, nums2, n):
    # Ініціалізуємо вказівники
    p1 = m - 1  # останній елемент у nums1
    p2 = n - 1  # останній елемент у nums2
    p = m + n - 1  # останнє місце у nums1 для заповнення

    # Проходимо через масиви, поки є елементи в nums2
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]  # Переміщуємо елемент з nums1
            p1 -= 1
        else:
            nums1[p] = nums2[p2]  # Переміщуємо елемент з nums2
            p2 -= 1
        p -= 1

# Приклад використання
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Виведе: [1, 2, 2, 3, 5, 6]

nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  # Виведе: [1]

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)  # Виведе: [1]
