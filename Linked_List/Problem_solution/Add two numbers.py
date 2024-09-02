# Add Two Numbers
# You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

# The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

# Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Return the sum of the two numbers as a linked list.

# Example 1:



# Input: l1 = [1,2,3], l2 = [4,5,6]

# Output: [5,7,9]

# Explanation: 321 + 654 = 975.
# Example 2:

# Input: l1 = [9], l2 = [9]

# Output: [8,1]
# Constraints:

# 1 <= l1.length, l2.length <= 100.
# 0 <= Node.val <= 9


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
def addTwoNumbersFirstApproch( l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(0)
        sumlist=dummy
        while l1 and l2:
            sum1 = l2.val+l1.val
            if sum1>9:
                fdig=sum1//10 
                sdig=sum1%10
                if fdig>0:
                    if l1.next and l2.next:
                        sumlist.next=ListNode(sdig)
                        sumlist=sumlist.next
                        l1.next.val+=fdig
                    else:
                        sumlist.next=ListNode(sdig)
                        sumlist.next.next=ListNode(fdig)
            else:
                sumlist.next=ListNode(sum1)
                sumlist=sumlist.next
            l1=l1.next
            l2=l2.next

        return dummy.next

   # sort list1 
def addTwoNumbers_mysecondApproch( l1:ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next  
def print_List(head):
    temp=head
    while temp:
        print(temp.val)
        temp=temp.next    



my_list1 = LinkedList(1)
my_list1.append(9)
my_list1.append(3)



my_list2 = LinkedList(4)
my_list2 .append(9) 
my_list2 .append(6) 



s=addTwoNumbers_mysecondApproch(my_list1.head,my_list2.head)
print_List(s)



