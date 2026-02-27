# Last updated: 28/02/2026, 01:35:28
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        l = 1
9        p = head
10
11        if not head or not head.next or k==0:
12            return head
13        while(p.next):
14            p = p.next
15            l+=1
16        if k==l:
17            return head
18        k = k%l
19        while(k>0):
20            p = head
21            while(p.next.next!=None):
22                p = p.next
23            last = p.next
24            p.next = None
25            last.next = head
26            head = last
27            k -= 1
28        return head