from collections import deque

n, m, k = map(int, input().split())
maze = [input().strip() for _ in range(n)]
ai, aj = next((i, row.index('A')) for i, row in enumerate(maze) if 'A' in row)
tunnels = {(i1, j1): (i2, j2) for _ in range(k) for i1, j1, i2, j2 in (map(int, input().split()),)}

def get_neighbors(i, j):
    neighbors = []
    if i > 0 and maze[i-1][j] != '#':
        neighbors.append((i-1, j))
    if i < n-1 and maze[i+1][j] != '#':
        neighbors.append((i+1, j))
    if j > 0 and maze[i][j-1] != '#':
        neighbors.append((i, j-1))
    if j < m-1 and maze[i][j+1] != '#':
        neighbors.append((i, j+1))
    return neighbors

def calculate_probability():
    visited = set()
    queue = deque([(ai, aj, 1.0)])

    while queue:
        i, j, prob = queue.popleft()

        if (i, j) in visited:
            continue
        visited.add((i, j))

        if maze[i][j] == '%':
            return prob

        neighbors = get_neighbors(i, j)
        num_neighbors = len(neighbors)
        if num_neighbors == 0:
            continue

        prob_per_neighbor = prob / num_neighbors
        for ni, nj in neighbors:
            queue.append((ni, nj, prob_per_neighbor))

    return 0.0

result = calculate_probability()
print('{:.10f}'.format(result))
