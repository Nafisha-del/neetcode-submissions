class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Calculate the middle index
            mid = (left + right) // 2
            
            # Check if target is present at mid
            if nums[mid] == target:
                return mid
            # If target is smaller, ignore right half
            elif nums[mid] > target:
                right = mid - 1
            # If target is larger, ignore left half
            else:
                left = mid + 1
                
        # Target was not present in the list
        return left
