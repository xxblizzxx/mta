def moves_to_stamp(stamp: str, target: str):
    stamp_len, target_len = len(stamp), len(target)
    target_list = list(target)
    visited = [False] * target_len
    result = []
    total_replaced = 0

    def can_stamp_at(pos):
        # Перевіряємо, чи можна "штампувати" в позиції pos
        for i in range(stamp_len):
            if target_list[pos + i] != '?' and target_list[pos + i] != stamp[i]:
                return False
        return True

    def do_stamp_at(pos):
        # Виконуємо штампування в позиції pos і рахуємо кількість замін на '?'
        replaced_count = 0
        for i in range(stamp_len):
            if target_list[pos + i] != '?':
                target_list[pos + i] = '?'
                replaced_count += 1
        return replaced_count

    while total_replaced < target_len:
        stamped = False
        for i in range(target_len - stamp_len + 1):
            if not visited[i] and can_stamp_at(i):
                replaced = do_stamp_at(i)
                total_replaced += replaced
                result.append(i)
                visited[i] = True
                stamped = True
                if total_replaced == target_len:
                    break
        if not stamped:
            return []

    # Повертаємо індекси в зворотному порядку
    return result[::-1]
