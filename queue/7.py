from collections import deque
from typing import List

def constrained_subset_sum(nums: List[int], k: int) -> int:
    n = len(nums)
    dp = nums[:]  # Копіюємо nums у dp, так як dp[i] має хоча б nums[i]
    deq = deque([0])  # Двостороння черга для зберігання індексів

    for i in range(1, n):
        # Оновлюємо dp[i] як dp[deq[0]] + nums[i] якщо це збільшує dp[i]
        dp[i] = max(dp[i], dp[deq[0]] + nums[i])

        # Видаляємо з черги елементи, які менші за поточний dp[i]
        while deq and dp[i] >= dp[deq[-1]]:
            deq.pop()

        deq.append(i)  # Додаємо поточний індекс

        # Видаляємо з черги елементи, які виходять за межі відстані k
        if deq[0] < i - k:
            deq.popleft()

    return max(dp)
