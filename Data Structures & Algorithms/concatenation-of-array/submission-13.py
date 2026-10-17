class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        for index in range(len(nums)):
            ans[index] = nums[index]
            ans[index + len(nums)] = nums[index]

        return ans