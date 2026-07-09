class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        i, j = 0, 0
        deque = deque([])
        res = []

        while j < len(nums):
            # Create the windows
            while (j - i) + 1 <= k:
                # Create the deque
                while len(deque)> 0 and nums[j] > deque[-1]:
                    deque.pop()

                deque.append(nums[j])

                j += 1

            res.append(deque[0])
            if nums[i] == deque[0]: deque.popleft()
            i += 1

        return res