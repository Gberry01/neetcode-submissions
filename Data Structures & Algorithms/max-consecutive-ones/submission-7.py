class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        best = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0

            if count > best:
                best = count

        return best    