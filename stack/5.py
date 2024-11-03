def decode_string(s: str) -> str:
    stack = []  # Стек для зберігання частин рядка і коефіцієнтів
    current_num = 0  # Поточне число (кратність)
    current_str = ""  # Поточний рядок

    for char in s:
        if char.isdigit():
            # Збираємо повне число (може бути більше однієї цифри)
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Додаємо поточне число і рядок у стек і починаємо новий
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            # Завершуємо обробку блоку і розкриваємо його
            prev_str, repeat_count = stack.pop()
            current_str = prev_str + current_str * repeat_count
        else:
            # Додаємо символ до поточного рядка
            current_str += char

    return current_str

# Приклади використання
print(decode_string("3[a]2[bc]"))     # Output: "aaabcbc"
print(decode_string("3[a2[c]]"))      # Output: "accaccacc"
print(decode_string("2[abc]3[cd]ef")) # Output: "abcabccdcdcdef"
