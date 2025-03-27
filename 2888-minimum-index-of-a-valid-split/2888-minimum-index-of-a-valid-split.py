class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        dominant = None
        max_count = 0

        for key, value in freq.items():
            if value > max_count:
                max_count = value
                dominant = key

        total_count = max_count 

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
        



