from collections import deque
from typing import List

def max_sliding_window(nums: List[int], k: int) -> List[int]:
    result = []
    deq = deque()  # Двостороння черга для індексів елементів у поточному вікні

    for i in range(len(nums)):
        # Видаляємо елементи з початку, якщо вони виходять за межі вікна
        if deq and deq[0] < i - k + 1:
            deq.popleft()
        
        # Видаляємо елементи з кінця, менші за поточний, оскільки вони не можуть бути максимумами
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()
        
        # Додаємо поточний елемент у кінець черги
        deq.append(i)
        
        # Додаємо максимум вікна в результат, коли ми досягли повного вікна розміру k
        if i >= k - 1:
            result.append(nums[deq[0]])

    return result
