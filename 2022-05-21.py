def lengthOfLongestSubstring( s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = []
        count = 0
        for i in s:
            if i in stack:
                while True:
                    if i == stack.pop(0):
                        break
            stack.append(i)
            print('stack:', stack)
            if count < len(stack):
                    count = len(stack)
        return count

print(lengthOfLongestSubstring('pwwkew'))


