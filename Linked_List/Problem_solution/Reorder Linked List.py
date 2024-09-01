# Reorder Linked List
# You are given the head of a singly linked-list.

# The positions of a linked list of length = 7 for example, can intially be represented as:

# [0, 1, 2, 3, 4, 5, 6]

# Reorder the nodes of the linked list to be in the following order:

# [0, 6, 1, 5, 2, 4, 3]

# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

# [0, n-1, 1, n-2, 2, n-3, ...]

# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

# Example 1:

# Input: head = [2,4,6,8]

# Output: [2,8,4,6]
# Example 2:

# Input: head = [2,4,6,8,10]

# Output: [2,10,4,8,6]
# Constraints:

# 1 <= Length of the list <= 1000.
# 1 <= Node.val <= 1000



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

def reorderList( head: ListNode) -> None:
        slow=head
        while slow.next:
            fast=slow
            if(fast.next and fast.next.next):
                while fast.next and fast.next.next:
                    fast=fast.next
                rN=fast.next
                fast.next=None
                sN=slow.next
                slow.next=rN
                slow.next.next=sN
                slow=slow.next.next
            else:
                slow=slow.next

def reorderList_newSol( head: ListNode) -> None: 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2           
            
my_list2 = LinkedList(1)
my_list2.append(2)
my_list2.append(3)
my_list2.append(4)
my_list2.append(5)
#reorderList(my_list2.head)
reorderList_newSol(my_list2.head)
print_List(my_list2.head)