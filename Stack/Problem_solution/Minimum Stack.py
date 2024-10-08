# problem 
# Minimum Stack
# Solved 
# Design a stack class that supports the push, pop, top, and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in 
# O
# (
# 1
# )
# O(1) time.

# Example 1:

# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]

# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1
# Constraints:

# -2^31 <= val <= 2^31 - 1.
# pop, top and getMin will always be called on non-empty stacks.

#---->Solution
class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop() if self.stack else None
        self.minstack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        # mi=self.stack[0]
        # for i in range(1,len(self.stack)):
        #     if self.stack[i]< mi:
        #         mi=self.stack[i]
        # return mi

        return self.minstack[-1]
min_stack = MinStack()

# Perform operations and see the results
min_stack.push(3)
min_stack.push(5)
print(min_stack.getMin())  # Should print the current minimum
min_stack.push(2)
min_stack.push(1)
min_stack.getMin()   # Should print the updated minimum
min_stack.pop()
min_stack.getMin()   # Should print the minimum after popping
min_stack.top()      # Should print the top element
min_stack.pop()
min_stack.pop()
