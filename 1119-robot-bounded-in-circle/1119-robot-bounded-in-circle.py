class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions: North, East, South, West
        dir_index = 0  # Starting from North
        
        for instruction in instructions:
            if instruction == "G":
                dx, dy = directions[dir_index]
                x, y = x + dx, y + dy
            elif instruction == "L":
                dir_index = (dir_index - 1) % 4  # Turn left (anticlockwise)
            elif instruction == "R":
                dir_index = (dir_index + 1) % 4  # Turn right (clockwise)
        
        # Check if the robot is bounded
        return (x == 0 and y == 0) or (dir_index != 0)



        