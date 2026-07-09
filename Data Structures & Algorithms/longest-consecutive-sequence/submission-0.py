class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Idea is using hashmap
        # using hashmap to store all the numbers first
        # then we identify the start of sequence using the hashmap
        # we put the start of sequene in a set, then we can check 
        # iteratively for each elemnt in start if it form longest consequnce
        numbers = {num for num in nums}
        seq_start = set()

        max_seq = 0
        for num in numbers:
            if num-1 not in numbers:
                seq_start.add(num)
    
        for seq in seq_start:
            s = seq
            length = 0
            while s in numbers:
                length += 1
                s += 1
            max_seq = max(length, max_seq)        

        return max_seq