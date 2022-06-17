class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(0)
a.left = TreeNode(0)
a.left.right = TreeNode(0)
a.left.left = TreeNode(0)


def minCameraCover( root):
        """
        :type root: TreeNode
        :rtype: int
        """
        print(root.val)

        def dfs(x, count):
            if x == None:
                return count
            
            print("val:", x.val)
            if x.val == 0 and x.left:
                x.left.val = 1
                print("left:",x.left.val)
            
            if x.val == 0 and x.right:
                x.right.val = 1
                print("right:",x.right.val)

            if x.val == 1:
                count +=1 
            
            print("count:", count)

            count = dfs(x.left, count)
            count = dfs(x.right, count)

            print(count)
            
            return count
        
        count = 0
        
        return dfs(root, count)



"""


"""


def longestStrChain( words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)
        dic = {}
        
        for i in words:
            dic[ i ] = 1
            
            for j in range(len(i)):
                
                # creating words by deleting a letter
                successor = i[:j] + i[j+1:]
                print("successor:", successor)
                if successor in dic:
                    dic[ i ] = max (dic[i], 1 + dic[successor])
        
        res = max(dic.values())
        return res


print(longestStrChain(["a","b","ba","bca","bda","bdca"]))