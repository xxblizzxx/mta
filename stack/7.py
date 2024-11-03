def longest_valid_parentheses(s: str) -> int:
    stack = [-1]  # Стек для зберігання індексів, -1 для початкової позиції
    max_length = 0  # Максимальна довжина валідного підрядка

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length
