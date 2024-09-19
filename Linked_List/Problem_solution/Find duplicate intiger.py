# Find Duplicate Integer
# You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

# Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

# Example 1:

# Input: nums = [1,2,3,2,2]

# Output: 2
# Example 2:

# Input: nums = [1,2,3,4,4]

# Output: 4
# Follow-up: Can you solve the problem without modifying the array nums and using 
# O( 1)
# O(1) extra space?

# Constraints:

# 1 <= n <= 10000
# nums.length == n + 1
# 1 <= nums[i] <= n
class FindDuplicate:
    def __init__(self, nums):
        self.nums = nums

    def find_duplicate(self):
        # Phase 1: Detect the intersection point in the cycle
        tortoise = self.nums[0]
        hare = self.nums[0]
                
        # Loop to find the intersection point
        while True:
            tortoise = self.nums[tortoise]  # Move tortoise one step
            hare = self.nums[self.nums[hare]]  # Move hare two steps
            
            if tortoise == hare:  # They meet at some point
                break

        # Phase 2: Find the entrance to the cycle (duplicate number)
        tortoise = self.nums[0]  # Start tortoise from the beginning
        
        while tortoise != hare:
            tortoise = self.nums[tortoise]  # Move tortoise one step
            hare = self.nums[hare]  # Move hare one step
        
        return hare  # The duplicate number

# To debug or test the code, you can instantiate the class with the nums array and call find_duplicate
if __name__ == "__main__":
    nums = [1, 2, 3, 2, 2]
    duplicate_finder = FindDuplicate(nums)
    result = duplicate_finder.find_duplicate()
    print(f"The duplicate number is: {result}")
