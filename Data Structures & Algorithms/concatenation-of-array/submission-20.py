class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
     # Start with an empty list that will hold our 2n answer
        ans = []

        # range(2) yields 0 and 1 -> the body runs twice.
        # We don't use i; it just means "repeat the block 2 times".
        for i in range(2):
            # Walk through every element of nums, left to right.
            # First pass  -> append [1,4,1,2]  (the original array)
            # Second pass -> append [1,4,1,2]  again (the copy)
            for num in nums:
                ans.append(num)  # add one element to the end of ans

        # After both passes ans = [1,4,1,2, 1,4,1,2], length 2 * n
        return ans