class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i]=="+":
                stack.append(stack[-1]+stack[-2])
                continue
            if operations[i]=="C":
                stack.pop()
                continue
            if operations[i]=="D":
                stack.append(stack[-1]*2)
                continue
            else:
                stack.append(int(operations[i]))
                
        return sum(stack)
        