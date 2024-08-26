# Linked List Cycle Detection

# Given the beginning of a linked list head, return true if 
# there is a cycle in the linked list. Otherwise, return false.
# There is a cycle in a linked list if at least one node in the list that 
# can be visited again by following the next pointer.
# Internally, index determines the index of the beginning of the cycle,
# if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, 
# then the tail node points to null and no cycle exists.
# Note: index is not given to you as a parameter.

# Example 1:
# Input: head = [1,2,3,4], index = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], index = -1
# Output: false

# Constraints:
# 1 <= Length of the list <= 1000.
# -1000 <= Node.val <= 1000
# index is -1 or a valid index in the linked list.



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self,value):
        new_node=ListNode(value)
        self.head=new_node
        self.length=1
    
    def print_list(self):
        if not self.head:
            return None
        temp=self.head
        while temp:
            print(temp.val)
            temp=temp.next

    def append(self,value):
        newNode=ListNode(value)
        if not self.head:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
        self.length+=1

       
def mergeTwoSortedLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    # Attach the remaining part of l1 or l2
    if l1:
        tail.next = l1
    else:
        tail.next = l2
    return dummy.next

def printList(listnode):
    temp=listnode
    while temp:
        print(temp.val)
        temp=temp.next

   
    
my_list1 = LinkedList(1)
my_list1.append(2)
my_list1.append(4)


my_list2 = LinkedList(1)
my_list2.append(3)
my_list2.append(5)


mergedlist =mergeTwoSortedLists(my_list1.head,my_list2.head)
printList(mergedlist)



