# Merge Two Sorted Linked Lists
# Solved 
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,5]

# Output: [1,1,2,3,4,5]

# Example 2:

# Input: list1 = [], list2 = [1,2]

# Output: [1,2]
# Example 3:

# Input: list1 = [], list2 = []

# Output: []

# Constraints:

# 0 <= The length of the each list <= 100.
# -100 <= Node.val <= 100


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

       
def mergeTwoLists( l1:ListNode, l2:ListNode) -> ListNode:
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


   # sort list1 
   
def print_List(head):
    temp=head
    while temp:
        print(temp.val)
        temp=temp.next    



my_list1 = LinkedList(1)
my_list1.append(2)
my_list1.append(4)


my_list2 = LinkedList(1)
my_list2.append(3)
my_list2.append(5)

returnNode=mergeTwoLists(my_list1.head,my_list2.head)
print_List(returnNode)



