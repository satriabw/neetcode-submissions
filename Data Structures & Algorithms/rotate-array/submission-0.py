class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
         array index is 0 .... n-1
         new index is ((i + k) % n)
         So for each element we need to swap with their new element
         how to swap without new space?
         nums[i] = 

         in = (i+k)%n
         i = ((in - k) % n + n) % n

         so for each i we know wich index we need to swap it, loop it until n-1-k
        '''
        n = len(nums)
        count = 0
        k = k % n
        start = 0
        while count < n:
            current = start
            prev = nums[start]

            while True:
                next_idx = (current+k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if current == start:
                    break
            start += 1
        
