class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        streak = 0
        for num in nums:
            if num == 1:
                count += 1
                streak = max(count, streak)
            else:
                count = 0
        return streak   