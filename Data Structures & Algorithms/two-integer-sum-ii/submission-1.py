class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = (0, len(numbers) - 1)
        result = []
        while i < j:
            if numbers[i] + numbers[j] == target:
                result = [i+1, j+1]
                break
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
        return result
        