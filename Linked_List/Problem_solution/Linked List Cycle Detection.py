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

       
def hasCycle( head:ListNode) -> bool:
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if fast is not None:
                if slow.val==fast.val:
                    return True
        return False



my_list = LinkedList(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)

print(hasCycle(my_list.head))

