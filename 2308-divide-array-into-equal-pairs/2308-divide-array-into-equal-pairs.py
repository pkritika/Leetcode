class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        elementsPair = int(len(nums) / 2)
        storedValue= []
        nums.sort()
        for i in range(0,len(nums), 2):
            if nums[i] == nums[i+1]:
                final_set = tuple(nums[i:i+2])
                storedValue.append(final_set) 
            else:
                return False
        if elementsPair == len(storedValue):
            return True
        else:
            return False
        # print(storedValue)
        # print(int(elementsPair))
        # print(len(storedValue))


            

        