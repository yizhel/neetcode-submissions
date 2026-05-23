class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2  # Find the middle index
            
            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                low = mid + 1  # Search the right half
            else:
                high = mid - 1  # Search the left half
                
        return -1  # Target not in list