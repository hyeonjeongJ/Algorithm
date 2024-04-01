class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        for i in range(len(str(x))):
            str_x = str(x)
            sum += int(str_x[i])
        if x % sum == 0:
            return sum
        else:
            return -1