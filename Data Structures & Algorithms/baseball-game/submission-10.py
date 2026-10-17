class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = []
        for i in operations:
            if i == "+":
                ops.append(ops[-1] + ops[-2])
            elif i == "D":
                ops.append(2 * ops[-1])
            elif i == "C":
                ops.pop()
            else:
                ops.append(int(i))
        return sum(ops)