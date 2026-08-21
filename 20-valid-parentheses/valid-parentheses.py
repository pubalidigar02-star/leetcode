class Solution:
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in pairs:
                if len(stack) == 0:
                    return False

                if stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0