def first_unique_char(s: str) -> int:
    # Крок 1: Підраховуємо частоти символів
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Крок 2: Знаходимо перший символ з частотою 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    # Якщо немає унікального символу, повертаємо -1
    return -1
