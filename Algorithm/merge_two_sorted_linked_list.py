# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def mergeLists(headA, headB):
    # A dummy node to store the result
    dummyNode = ListNode(0)

    # Tail stores the last node
    tail = dummyNode
    while True:

        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        # Compare the data of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
        if headA.val <= headB.val:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next

        # Advance the tail
        tail = tail.next

    # Returns the head of the merged list
    return dummyNode.next


"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        # import pdb
        # pdb.set_trace()
        new_list = ListNode(None)
        print("\n**new_list: ", new_list)
        new_list_tmp = new_list
        print("\n**new_list_tmp: ", new_list_tmp)
        while True:
            if not list1:
                new_list_tmp.next = list2
                break
            if not list2:
                new_list_tmp.next = list1
                break
            if list1 and list2 and list1.val <= list2.val:
                print("\n** next node should be ", list1.val)
                new_node = ListNode(list1.val)
                new_list_tmp.next = new_node
                list1 = list1.next
            if list2 and list1 and list2.val <= list1.val:
                print("\n** next node should be ", list2.val)
                new_node = ListNode(list2.val)
                new_list_tmp.next = new_node
                list2 = list2.next
            new_list_tmp = new_list_tmp.next

        return new_list


head_1 = ListNode(5)
head_1.next = ListNode(8)
head_1.next.next = ListNode(12)
head_1.next.next.next = ListNode(17)

print("List 1 ->")
merged_list_tmp = head_1
while merged_list_tmp:
    print(merged_list_tmp.val)
    merged_list_tmp = merged_list_tmp.next

head_2 = ListNode(3)
head_2.next = ListNode(6)
head_2.next.next = ListNode(7)
head_2.next.next.next = ListNode(11)

print("List 2 ->")
merged_list_tmp = head_2
while merged_list_tmp:
    print(merged_list_tmp.val)
    merged_list_tmp = merged_list_tmp.next

# merged_list = Solution().mergeTwoLists(head_1, head_2)
merged_list = mergeLists(head_1, head_2)
print("\n** Merged list->")
merged_list_tmp = merged_list
while merged_list_tmp:
    print(merged_list_tmp.val)
    merged_list_tmp = merged_list_tmp.next

