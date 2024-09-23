# Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.
# Example 1:

# Input: tokens = ["1","2","+","3","*","4","-"]

# Output: 5

# Explanation: ((1 + 2) * 3) - 4 = 5
# Constraints:

# 1 <= tokens.length <= 1000.
# tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].


# SOLUTION
def evalRPN( tokens) -> int:
        stack1=[]
        for i in tokens:
            if i.isdigit():
                stack1.append(int(i))
            else:
                if i == "+":
                    stack1.append( stack1.pop() + stack1.pop())
                elif i == "-":
                    stack1.append(stack1.pop() - stack1.pop())
                elif i == "*":
                    stack1.append(stack1.pop() * stack1.pop())
                elif i == "/":
                    stack1.append(stack1.pop() / stack1.pop())
        return stack1[0]
    
    
print(evalRPN(["1","2","+","3","*","4","-"]))