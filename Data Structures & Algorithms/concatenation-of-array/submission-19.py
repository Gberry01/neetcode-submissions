class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        alist = []
        for i in range(2):
            for num in nums:
                alist.append(num)
        return alist