class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, speed) for pos, speed in zip(position, speed)]
        fleet = []

        for pos, speed in sorted(cars, reverse=True):
            time = (target - pos) / speed
            fleet.append(time)
            if len(fleet) > 1 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        
        return len(fleet)