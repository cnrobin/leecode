'''
��������ǽ��������������������᷵��һ���µ���������ʾ���ǵĺ͡�

�����Լ���������� 0 ֮�⣬���������������� 0 ��ͷ��

ʾ����

���룺(2 -> 4 -> 3) + (5 -> 6 -> 4)
�����7 -> 0 -> 8
ԭ��342 + 465 = 807


��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/add-two-numbers
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:


        v1=l1
        v2=l2
        l3=None
        old=None
        jin_wei=0
        while(v1!=None or v2!=None):
            v1x=0
            v2x=0
            if(v1!=None):
                v1x=v1.val
                v1=v1.next
            if(v2!=None):
                v2x=v2.val
                v2=v2.next

            v3x=(v1x+v2x+jin_wei)
            jin_wei=int(v3x/10)
            v3x=v3x%10
            v3=ListNode(v3x)
            if(l3==None):
                l3=v3
            if old!=None:
                old.next=v3
            old=v3
        if(jin_wei!=0):
            v3=ListNode(jin_wei)
            old.next=v3
        result=[]
        old=l3
        while(old!=None):
            result.append(old.val)
            old=old.next

        return l3