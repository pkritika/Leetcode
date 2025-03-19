class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # l = 0 
        # r = 0
        # ct_1 = 0
        # numsFlip = 0
        # while r <= len(nums):
        #     if r - l  == 3:
        #         if nums[l] != 1:
        #             ct_1 = 3 - ct_1                l+= 1
        #         l+= 1

        #         if nums[r] == 1:
        #             ct_1+= 0

        n = len(nums)
        res = 0
        for i in range(n - 2):
            if nums[i] == 0:
                res += 1
                nums[i] = 1
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
        
        if nums[-1] == 1 and nums[-2] == 1:
            return res
        else:
            return -1

            


