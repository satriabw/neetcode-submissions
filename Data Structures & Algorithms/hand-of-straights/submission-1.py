class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq = [0] * 1000

        # We count how many element used, if it used that maximum group then we cannot make contigous element
        for num in hand:
            freq[num] += 1
        
        for num in range(hand[0], hand[-1]+1):
            if freq[num] > 0:
                count = freq[num]
                for j in range(num, num + groupSize):
                    if freq[j] < count:
                        return False
                    freq[j] -= count
        return True
        