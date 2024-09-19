#Q

# Validate Parentheses
# Solved 
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true
# Example 3:

# Input: s = "[(])"

# Output: false
# Explanation: The brackets are not closed in the correct order.

# Constraints:

# 1 <= s.length <= 1000

# SOLUTION



def isValid( brackets: str) -> bool:
    bracket_map = {")": "(", "]": "[", "}": "{"}
    open_brackets = []

    for char in brackets:
        if char not in bracket_map:
            open_brackets.append(char)
            continue
        if not open_brackets or open_brackets[-1] != bracket_map[char]:
            return False
        open_brackets.pop()
    
    return len(open_brackets) == 0


print(f's="[]"')
print(isValid("[]"))

print('s = "[(])"')
print(isValid("[(])"))

