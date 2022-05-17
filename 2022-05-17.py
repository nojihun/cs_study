"""
구간 병합 리트코드 56번

"""

def merge(intervals):

    """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
    merged = []
    for i in sorted(intervals, key=lambda x: x[0]):
             
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged +=i,
                
    return merged

print(merge([[1,3],[2,6],[8,10],[15,18]]))



""""
리트코드 179번

큰수 만들기
"""


def largestNumber(self, nums):
    """
        :type nums: List[int]
        :rtype: str
    """
    if sum(nums) == 0:
        return '0'
        
    nums = list(map(str, nums))
    nums = sorted(nums, key = lambda x:x*9, reverse = True)
    answer = ''.join(nums)                
    return answer


"""

"""
import heapq
def kClosest(points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for (x, y) in points:
            dist = x**2 +y**2
            heapq.heappush(heap, (dist, x, y))
        print('heap:', heap)
        result = []
        for _ in range(k):
            (dist, x,  y) = heapq.heappop(heap)
            result.append((x,y))
        
        return result

print(kClosest([[3,3],[5,-1],[-2,4]], 2))