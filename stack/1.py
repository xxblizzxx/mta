def is_valid(s):
    # Словник для зберігання пар дужок
    bracket_map = {')': '(', ']': '[', '}': '{'}
    stack = []

    # Проходимо по кожному символу в рядку
    for char in s:
        if char in bracket_map:
            # Беремо верхній елемент стека, якщо він не порожній, інакше '#'
            top_element = stack.pop() if stack else '#'
            # Перевіряємо, чи відповідає закрита дужка відкритій
            if bracket_map[char] != top_element:
                return False
        else:
            # Додаємо відкриту дужку в стек
            stack.append(char)

    # Якщо стек порожній, всі дужки збалансовані
    return not stack

# Приклади використання
print(is_valid("()"))       # Output: True
print(is_valid("()[]{}"))   # Output: True
print(is_valid("(]"))       # Output: False
print(is_valid("([)]"))     # Output: False
print(is_valid("{[]}"))     # Output: True
