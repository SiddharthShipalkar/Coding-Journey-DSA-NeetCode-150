

#Copy Linked List with Random Pointer

# You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

# Create a deep copy of the list.

# The deep copy should consist of exactly n new nodes, each including:

# The original value val of the copied node
# A next pointer to the new node corresponding to the next pointer of the original node
# A random pointer to the new node corresponding to the random pointer of the original node
# Note: None of the pointers in the new list should point to nodes in the original list.

# Return the head of the copied linked list.

# In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

# Example 1:
# Input: head = [[3,null],[7,3],[4,0],[5,1]]
# Output: [[3,null],[7,3],[4,0],[5,1]]
# Example 2:


# Input: head = [[1,null],[2,2],[3,2]]
# Output: [[1,null],[2,2],[3,2]]
# Constraints:

# 0 <= n <= 100
# -100 <= Node.val <= 100
# random is null or is pointing to some node in the linked list.

class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value, random_index=None):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node


    def print_list(self):
        temp = self.head
        while temp:
            random_val = temp.random.val if temp.random else None
            print(f"[{temp.val}, {random_val}]")
            temp = temp.next

    def copyRandomList(self):
        old_to_copy = {None: None}

        cur = self.head
        while cur:
            copy = ListNode(cur.val)
            old_to_copy[cur] = copy
            cur = cur.next

        cur = self.head
        while cur:
            copy = old_to_copy[cur]
            copy.next = old_to_copy[cur.next]
            copy.random = old_to_copy[cur.random]
            cur = cur.next

        copied_list = LinkedList()
        copied_list.head = old_to_copy[self.head]
        return copied_list


ll = LinkedList()
ll.append(3, None)  
ll.append(7, 0)     
ll.append(4, 1)     
ll.append(5, 2)     

print("Original Linked List:")
ll.print_list()

copied_ll = ll.copyRandomList()
print("\nCopied Linked List:")
copied_ll.print_list()
