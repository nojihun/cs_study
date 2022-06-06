"""
bfs 를 활용한 가장 먼 노드 갯수 찾기
"""

import collections
a = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


from collections import deque

def solution(n, edge):
    graph = dict()
    visited = [0] * (n+1)
    
    for i in range(1, n+1): # 빈 딕셔너리 생성 {노드 번호: [연결노드]}
        graph[i] = []
    
    for i in edge:  # 딕셔너리 키 - 값 할당
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    return bfs(graph, n, visited)

def bfs(graph, n, visited):
    queue = deque([1])  # 큐에 시작 노드 1 삽입
    visited[1] = 1
    
    while queue:
        v = queue.popleft()
        print(graph)
        
        for i in graph[v]:
            
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                queue.append(i)
            print(visited)
    return visited.count(max(visited))

solution(6, a)


"""

"""
import copy
import heapq
import numpy as np
def solution(jobs):
    jobs_2 = copy.deepcopy(jobs)
    printer = []
    result = []
    count = 0
    while jobs:
        print(jobs)
        print('count:', count)
        if count >= jobs[0][0] and printer == []:
            heapq.heappush(result, count+jobs[0][1]-jobs_2[0][0])
            print("cdcd",count+jobs[0][1]-jobs_2[0][0] )
            print('count:', count)
            print("c-2",jobs[0][1] )
            print('ㅊㅇㅇ,', jobs_2[0][0])
            print(jobs_2)
            printer.append(jobs.pop(0))
            jobs_2.pop(0)
        elif printer[0][1] == 1:
            printer.pop()
        else:
            printer[0][1] -= 1
        count+=1
        for i in jobs:
            if i[0] != 0:
                i[0] -=1

    print('result:',result)
    print('jobs_2', jobs_2)
    return np.mean(result)

solution([[0, 3], [1, 9], [2, 6]])
