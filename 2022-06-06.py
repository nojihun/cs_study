# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
두개의 연결리스트가 있다.
두개의 연결리스트가 중간에 만난다고 할때 만나는 점을 구하라
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        add = set()
    
        while headA:
            add.add(headA)
            headA = headA.next
    
        while headB:
            if headB in add:
                return headB
            headB = headB.next
        return None


### set을 생각도 못했다.

"""
n개의 퀸이 있고 n x n 의 체스판이 있다.
퀸이 서로 잡지않게 배치할 수 있는 방법이 몇가지나 있는가


"""



def totalNQueens(n: int) -> int:                
        visited_cols=set()
        visited_diagonals=set()
        visited_antidiagonals=set()
        
        def backtrack(r):
            if r==n:  # valid solution state   
                return 1
                        
            cnt=0
            for c in range(n):
                if not(c in visited_cols or (r-c) in visited_diagonals or (r+c) in visited_antidiagonals):
                    visited_cols.add(c)
                    visited_diagonals.add(r-c)
                    visited_antidiagonals.add(r+c)                    
                    cnt+=backtrack(r+1) # count the overall tally from this current state
                    
                    visited_cols.remove(c)
                    visited_diagonals.remove(r-c)
                    visited_antidiagonals.remove(r+c)                    
            
            return cnt
        
        return backtrack(0)


print(totalNQueens(6))


