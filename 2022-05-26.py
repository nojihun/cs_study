"""
bit 연산
리스트에 하나의 값 빼고 다 두쌍씩 있을때 그 하나의 값을 구하라
0 ^ 0
0
4 ^0 
4 

4^ 4
0

비트 연산자는 비트 단위로 연산을 수행하며 비트 논리곱(&), 비트 논리합(|), 비트 상호배제(^), 비트 부정(~), 왼쪽 쉬프트(<<), 오른쪽 쉬프트(>>)가 있습니다.

비트 논리곱은 같은 자리가 모두 1일 때 해당 자리의 연산 결과가 1이며 그렇지 않을 때 0입니다. 예를 들어 a가 6이고 b가 3일 때 a&b는 2입니다. (110 & 011 => 010)

비트 논리합은 같은 자리에 하나라도 1이면 해당 자리의 연산 결과가 1이며 둘 다 0일 때만 0입니다. 예를 들어 a가 6이고 b가 3일 때 a|b는 7입니다.(110 | 011 => 111)

비트 상호배제는 같은 자리의 값이 서로 다르면 해당 자리의 연산 결과가 1이며 같을 때 0입니다. 예를 들어 a가 6이고 b가 3일 때 a^b는 5입니다.(110^011 => 101)

비트 부정은 0인 자리는 1로 1인 자리는 0으로 변환합니다
"""
def singleNumber( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num #같은 값을 만나면 0 으로 변환
        
        return result

"""
그리디 알고리즘

리스트가 주어지는데 리스트의 위치에 날이 하나씩 대응이 된다. 그리고 그때의 가격이 그 위치의 값이다.
주식을 여러번 사고 팔았을때 가장 수익이 높은 것은?
"""

def maxProfit( prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(prices) -1):
            if prices[i+1] > prices[i]:
                result += prices[i+1] - prices[i]
        return result


"""

"""
import heapq

def reconstructQueue( people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
            
        result = []
        print(heap)
        while heap:
            person  = heapq.heappop(heap)
            print('p:',person)
            result.insert(person[1], [-person[0],person[1]])
            
        return result

reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])



"""
"""
import collections
def leastInterval( tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks)
        result = 0
        
        while True:
            sub= 0
            for task, _ in counter.most_common(n+1):
   
                sub +=1
                result +=1

                counter.subtract(task)
  
                counter += collections.Counter()
                
            if not counter:
                break
                
            result += n - sub +1
            
    
        return result



from heapq import heapify, heappush, heappop
from collections import deque

def leastInterval( tasks, n) -> int:

		count = collections.Counter(tasks)

		#the pq represents whatever task availabe to do at the current time
		pq = [-cnt for cnt in count.values()]
		heapify(pq)
        
		#the q represents whatever unavalble task to do at the current time
		q = deque()

		time = 0
		while q or pq:
			#check if there is a task on waiting list that becomes available
			if q and q[0][1] == time:
				cnt, _ = q.popleft()
				heappush(pq, cnt)

			#at a current time, check if there is any available task
			if pq:
				cnt = heappop(pq)
				next_avail = time+n+1

				#decrement count
				cnt+=1

				#push it into waiting list if there is still task
				if cnt: q.append((cnt,next_avail))

				#increment time
				time+=1
			#if there isn't any available task on pq, check if there is
			#task on waiting list on the queue. If there is, fast forward
			#to the time where it is available
			elif q:
				time = q[0][1]

		return time



"""
"""

def canCompleteCircuit( gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        for i in range(len(gas)):
            remain = 0
            for j in range(i, len(gas) + i):
                index = j%len(gas)
                
                can_travel = True
                if gas[index] + remain < cost[index]:
                    can_travel = False
                    break
                else:
                    remain+=gas[index] - cost[index]
            if can_travel:
                return i
        return -1

print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))