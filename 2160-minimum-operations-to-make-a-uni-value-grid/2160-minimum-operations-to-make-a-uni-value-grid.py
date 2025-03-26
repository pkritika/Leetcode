class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        all_nums = [grid[i][j] for i in range(m) for j in range(n)]
        all_nums.sort()
        median_val = all_nums[len(all_nums)//2]
        total_changes = 0
        for n in all_nums:
            if ((abs(n-median_val) % x) != 0):
                return -1
            total_changes += (abs(n-median_val) // x)
        return total_changes

        