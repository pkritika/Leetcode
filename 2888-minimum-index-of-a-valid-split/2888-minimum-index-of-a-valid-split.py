class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1   #freq = {1: 1, 2: 3}
        dominant = None
        max_count = 0

        for key, value in freq.items():
            if value > max_count:
                max_count = value
                dominant = key #since the value of 2 is more than other value we take 2 as our dominant number and the total count is the 3

        total_count = max_count   #Dominant element = 2
                                 #Total occurrences = 3

        prefix_count = 0
        n = len(nums)
        for i in range(n - 1):    
            if nums[i] == dominant:
                prefix_count += 1
                total_count -= 1  
        
            size_left = i + 1
            size_right = n - (i + 1)

            if prefix_count * 2 > size_left and total_count * 2 > size_right:
                return i  
        return -1 
        

# iteration 1 (i = 0, nums[i] = 1)
        #nums[0] = 1, which is not the dominant element.So, prefix_count and total_count remain unchanged.
        # Left subarray: [1] → 2 is not dominant
        # Right subarray: [2, 2, 2] → 2 is dominant, but left is invalid.
        # No valid split at i = 0
#iteration 2 (i =1 , nums [i] = 2)
        # #nums[1] = 2, which is the dominant element.So, prefix_count and total_count changes as prefix_count = 1 , total_count = 2.
        # Left subarray: [1, 2] → 2 appears once → 1 * 2 = 2, which is not greater than 2 (not dominant).
        # Right subarray: [2, 2] → 2 appears twice → 2 * 2 = 4 > 2 (dominant).
        # No valid split at i = 1
#iteration 3 (i =2 , nums [i] = 2)
        # #nums[1] = 2, which is the dominant element.So, prefix_count and total_count changes as prefix_count = 2 , total_count = 1.
        # Left subarray: [1, 2, 2] → 2 appears twice → 2 * 2 = 4 > 3 (dominant).
        # Right subarray: [2] → 2 appears once → 1 * 2 = 2 > 1 (dominant).
        # Since 2 is dominant in both halves, we return i = 2.



