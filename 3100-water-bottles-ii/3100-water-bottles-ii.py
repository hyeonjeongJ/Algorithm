class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total, emptyBottles = numBottles, numBottles
        
        while emptyBottles >= numExchange :
            emptyBottles = emptyBottles - numExchange + 1
            numExchange += 1
            total += 1
        return total