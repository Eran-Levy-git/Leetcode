from ast import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        retSum = []
        for i in nums:
            sum += i
            retSum.append(sum)
        return retSum
