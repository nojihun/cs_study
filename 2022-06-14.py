def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        
        answer = []
        for i in range(len(s)):
            stack = [s[i]]
            for j in s[i+1:]:
                print(stack)
                print(answer)
                print(s[i])
                print(j)
                stack.append(j)
                a =  list(reversed(stack))
                if s[i] == j and stack == a and len(stack) > len(answer):
                    answer = list(stack)
                    print('break')
                    
        return answer

    



"""
"""

def minDistance(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            return 0
        
        if len(word1) >= len(word2):
            a = word1
            b= word2
        else:
            a= word2
            b= word1
            
        answer= 0
        
        if b in a:
            return 

        for i in range(len(b)):
            for j in range(len(b[i+1:]),0,  -1):
                c = "".join(b[i:j+1])
                print("j:",j)
                print("b:", b[i:j+1])
                print("c:", c)
                if c in a:
                    answer = max(len(c), answer)
                    break

        
        return answer


print(minDistance("ab", "bc"))


if 'ea' in "eat":
    print("ㅇㄹㄴㅇㄹㄴ")