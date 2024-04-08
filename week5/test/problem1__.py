"""
출발에서 도착까지 가능한 경로의 개수를 DP를 이용하여 구하시오

1. grid[0][0]에서 출발
2. grid[m-1][n-1]에 도착
3. 이동은 오른쪽과 아래로만 가능
4. Obstacle이 있는 경우 이동 불가능
"""


def pathFinder(m, n):
    # Initialize the memoization table with -1, indicating unvisited cells
    memo = [[-1 for _ in range(n)] for _ in range(m)]

    # Check if the current position is within the grid and not an obstacle
    def is_valid(x, y):
        return 0 <= x < m and 0 <= y < n and obstacleGrid[x][y] == 0

    # Recursive function to find the path count with memoization
    def get_path(x, y):
        # Base case: when the bottom-right cell is reached
        if x == m - 1 and y == n - 1:
            return 1
        # If the cell is already computed, return the stored value
        if memo[x][y] != -1:
            return memo[x][y]
        # Initialize path count for the cell to 0
        memo[x][y] = 0
        # Check the right and down cells for valid paths
        if is_valid(x, y + 1):
            memo[x][y] += get_path(x, y + 1)
        if is_valid(x + 1, y):
            memo[x][y] += get_path(x + 1, y)
        # Return the path count for the current cell
        return memo[x][y]

    # If the start or end cell has an obstacle, return 0 as no path is possible
    if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
        return 0

    # Calculate the number of paths from the top-left corner
    return get_path(0, 0)




#### Do not edit here ####
import random

random.seed(500)

# print("격자의 크기를 입력하세요 (m n): ", end="")
# m, n = map(int, input().split())
n = 10
m = 10

obstacle_rate = 0.3 
obstacleGrid = [[0 if random.random() >= obstacle_rate else 1 for _ in range(n)] for _ in range(m)]
obstacleGrid[0][0] = 0 
obstacleGrid[m-1][n-1] = 0

result = pathFinder(n, m)
print(f'경로의 개수는 {result}개 입니다.')



