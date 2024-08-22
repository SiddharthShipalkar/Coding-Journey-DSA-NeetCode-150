# Problem -: Reverse a Linked List

# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# Example 1:

# Input: head = [0,1,2,3]

# Output: [3,2,1,0]
# Example 2:

# Input: head = []

# Output: []
# Constraints:

# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000

#--> Solution 

#Definition for singly-linked list.

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

    
        
def reverseList_using_iterativeApproch(head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

def reverseList_Using_RecursiveApproch( head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = reverseList_Using_RecursiveApproch(head.next)
    head.next.next = head
    head.next = None
    return new_head

def Print_reversedList(head):
    if not head:
        return None
    temp=head
    while temp:
        print(temp.val)
        temp=temp.next

my_list= LinkedList(1)
my_list.append(2)
my_list.append(3)
#my_list.print_list()
#Returnhead= reverseList(my_list.head)
returnhead= reverseList_Using_RecursiveApproch(my_list.head)
Print_reversedList(returnhead)






