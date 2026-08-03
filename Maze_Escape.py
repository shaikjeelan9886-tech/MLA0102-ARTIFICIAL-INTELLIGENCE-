from collections import deque

maze = [
    ['S', 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 'G']
]

rows = len(maze)
cols = len(maze[0])

start = (0, 0)
goal = (3, 3)

queue = deque([(start, 0)])
visited = set([start])

directions = [(1,0),(-1,0),(0,1),(0,-1)]

while queue:
    (x, y), steps = queue.popleft()

    if (x, y) == goal:
        print("Goal Reached!")
        print("Shortest Steps =", steps)
        break

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if maze[nx][ny] != 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
