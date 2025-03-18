class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0  # Left pointer
        usedBits = 0  # Tracks OR of elements in window
        maxLength = 0
        
        for r in range(len(nums)):
            # If there's an overlap, move left pointer until valid
            while (usedBits & nums[r]) != 0:
                usedBits ^= nums[l]  # Remove nums[l] from OR
                l += 1
            
            # Add nums[r] to OR
            usedBits |= nums[r]
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength