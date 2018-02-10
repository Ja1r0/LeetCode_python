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
            target=0-nums[i]
            numbers=nums[i+1:]
            s=set()
            for value in numbers:
                if target-value in s:
                    solution.append([nums[i],value,target-value])
                else:
                    s.add(value)
        final_solution=[]
        for s in solution:
            if set(s) not in final_solution:
                final_solution.append(set(s))
        sol=[]
        for e in final_solution:
            sol.append(list(e).sort())
        return sol
