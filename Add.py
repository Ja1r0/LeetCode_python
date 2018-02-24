##############
# Add Binary #
##############
'''
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
'''
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2)+int(b,2))[2:]
###################
# Add Two Numbers #
###################
'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resoult=res=ListNode(0)
        carry=0
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            div,rem=divmod(carry,10)
            carry=div
            res.next=ListNode(rem)
            res=res.next
        return resoult.next
###############
# Add Strings #
###############
'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry=0
        res=[]
        num1=list(num1)
        num2=list(num2)
        while len(num1)>0 or len(num2)>0:
            if len(num1)>0:
                carry+=ord(num1.pop())-ord('0')
            if len(num2)>0:
                carry+=ord(num2.pop())-ord('0')
            div,rem=divmod(carry,10)
            carry=div
            res.append(rem)
        if carry:
            res.append(carry)
        return ''.join([str(i) for i in res])[::-1]
####################
# Multiply Strings #
####################
'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1=len(num1)
        l2=len(num2)
        if l1<=l2:
            rnum1=num1[::-1]
            rnum2=num2[::-1]
        else:
            rnum2=num1[::-1]
            rnum1=num2[::-1]
        a=0
        for idx1 in range(len(rnum1)):
            n1=ord(rnum1[idx1])-ord('0')
            carry=0
            for idx2 in range(len(rnum2)):
                n2=ord(rnum2[idx2])-ord('0')
                carry,rem=divmod(n2*n1+carry,10)
                a+=rem*(10**(idx1+idx2))
            if carry:
                a+=carry*(10**(idx1+idx2+1))
        return str(a)

            
        
        
