class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = 0
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                count = stack[-1][1] + 1
                stack.append((c, count))
                if count == k:
                    for _ in range(k):
                        stack.pop()
            else:
                count = 1
                stack.append((c, count))
        
        result = ""
        for c, count in stack:
            result += c
        return result
