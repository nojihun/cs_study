def maxSubArray( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(1, len(nums)):
            nums[i]+= nums[i-1] if nums[i-1] > 0 else 0
            print('nums[i]:',i,':', nums[i])
        print('nums:', nums)
        return max(nums)

maxSubArray( [-2,1,-3,4,-1,2,1,-5,4])

4



import sys

L = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())

a = 0
count_1 = 0
while True:
    if n+a in S or n+a >= max(S):
        break
    
    a +=1
    count_1 +=1


b = 0
count_2 = 0
while True:    
    if n-b in S or n-b <= 0:
        break
    b+=1
    count_2 +=1


if a == 0:
    print(b)
elif b == 0:
    print(a)
elif b== 0 and a== 0:
    print(0)
else:
    print(a*b-1)