# Remove Node From End of Linked List
# Solved 
# You are given the beginning of a linked list head, and an integer n.

# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:

# Input: head = [1,2,3,4], n = 2

# Output: [1,2,4]
# Example 2:

# Input: head = [5], n = 1

# Output: []
# Example 3:

# Input: head = [1,2], n = 2

# Output: [2]
# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz




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

def print_List(head):
    temp=head
    while temp:
        print(temp.val)
        temp=temp.next
def removeNthFromEnd( head: ListNode, n: int) -> ListNode:
        dummyNode=ListNode(0,next=head)
        slow=dummyNode
        fast=head
        while fast and n>0:
            fast=fast.next
            n-=1
        while fast:
            slow=slow.next
            fast=fast.next
        removedNode=slow.next
        slow.next=slow.next.next
        removedNode.next=None
        return dummyNode.next


my_list2 = LinkedList(1)
my_list2.append(3)
my_list2.append(5)

newList=removeNthFromEnd(my_list2.head,1)
print_List(newList)



