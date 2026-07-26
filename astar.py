from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

def astar(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    cost = {start: 0}
    visited = set()

    while not pq.empty():
        f, node = pq.get()

        if node in visited:
            continue

        print(node)
        visited.add(node)

        if node == goal:
            print("Goal Reached")
            return

        for neighbor, weight in graph[node]:
            new_cost = cost[node] + weight
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                pq.put((priority, neighbor))

astar('A', 'F')
