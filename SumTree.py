###########
# Two Sum #
###########
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for idx,value in enumerate(nums):
            if target-value in d:
                return [d[target-value],idx]
            else:
                d[value]=idx
######################################
# Two Sum II - Input array is sorted #
######################################
'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for idx,value in enumerate(numbers):
            if target-value in d:
                return [d[target-value]+1,idx+1]
            else:
                d[value]=idx
###############################
# Two Sum IV - Input is a BST #
###############################
'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
Output: False
'''
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        bfs=[root]
        s=set()
        for node in bfs:
            if k-node.val in s:
                return True
            s.add(node.val)
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
        return False
#########
# 3 Sum #
#########
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue            
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum<0:
                    l+=1
                elif sum>0:
                    r-=1
                else:
                    solution.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1                    
        return solution
########
# 4sum #
########
'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.
Note: The solution set must not contain duplicate quadruplets.
For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        l=len(nums)
        res=set()
        d={}
        if l<4:
            return []
        for i in range(l-1):
            for j in range(i+1,l):
                sum2=nums[i]+nums[j]
                if sum2 in d:
                    d[sum2].append((i,j))
                else:
                    d[sum2]=[(i,j)]
        for i in range(l-3):
            for j in range(i+1,l-2):
                sum2=target-nums[i]-nums[j]
                if sum2 in d:
                    for t in d[sum2]:
                        if t[0]>j:
                            res.add((nums[i],nums[j],nums[t[0]],nums[t[1]]))
        return [list(t) for t in res]
###########
# 4sum II #
###########
'''
Given four lists A, B, C, D of integer values, 
compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. 
All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
Example:
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
Output:
2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''
class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A.sort()
        B.sort()
        C.sort()
        D.sort()
        d={}
        res=0
        l=len(A)
        for i in range(l):
            for j in range(l):
                if C[i]+D[j] not in d:
                    d[C[i]+D[j]]=[(i,j)]
                else:
                    d[C[i]+D[j]].append((i,j))
        for i in range(l):
            for j in range(l):
                sum2=0-A[i]-B[j]
                if sum2 in d:
                    res+=len(d[sum2])
        return res
