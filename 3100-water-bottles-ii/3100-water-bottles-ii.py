class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0
        bottlesDrunk = 0
        
            
        while (numBottles > 0):
            emptyBottles += numBottles 
            bottlesDrunk += numBottles 
            numBottles = 0
            while(emptyBottles // numExchange > 0) :  
                emptyBottles -= numExchange
                numExchange += 1
                numBottles += 1 

                
        return bottlesDrunk      