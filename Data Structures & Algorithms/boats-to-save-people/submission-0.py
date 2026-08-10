class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        result = 0
        people.sort()
        i, j = 0, len(people) - 1
        while i <= j:
            result += 1
            if ((people[i] + people[j]) <= limit) or i == j:
                i += 1
                j -= 1
            else:
                j -= 1
        return result