class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
         # Binary Search -> min 1 minute, max-> all cars by min ranked
        # find total repairs in time T
        l = 1
        r = min(ranks) * cars * cars
        while l < r:
            m = l + (r-l) // 2
            total_cars_repaired = 0
            for i in range(len(ranks)):
                total_cars_repaired += math.floor(math.sqrt(m/ranks[i]))
            if total_cars_repaired < cars:
                l = m+1
            else:
                r = m
        return l