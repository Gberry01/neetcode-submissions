class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
       
        last = -1
        for index in range(len(arr) -1, -1, -1):
            current = arr[index]
            arr[index] = last
            last = max(current, arr[index])
        return arr