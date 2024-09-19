# Reverse Nodes in K-Group
# You are given the head of a singly linked list head and a positive integer k.
# You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.
# Return the modified list after reversing the nodes in each group of k.
# You are only allowed to modify the nodes' next pointers, not the values of the nodes.
# Example 1:
# Input: head = [1,2,3,4,5,6], k = 3
# Output: [3,2,1,6,5,4]
# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# Constraints:

# The length of the linked list is n.
# 1 <= k <= n <= 100
# 0 <= Node.val <= 100



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

def reverseKGroup( head: ListNode, k: int) -> ListNode:
    temp = head
    pre=None
    nxt=None
    while temp:
        for _ in range(k):
            if temp.next:
                


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)