class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [(position[i], speed[i]) for i in range(len(speed))]
        cars = sorted(cars, key=lambda tup: tup[0])[::-1]

        for car in cars:
            stack.append(car)
            
            if len(stack) > 1:
                car1 = stack.pop()
                car2 = stack.pop()

                if ((target-car1[0])/car1[1]) <= ((target-car2[0])/car2[1]):
                    stack.append(car2)
                else:
                    stack.append(car2)
                    stack.append(car1)

        return len(stack)