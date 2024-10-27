from collections import deque

class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_list = {v: [] for v in range(vno)}

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))

    def print_adj_list(self):
        for vertex, n in self.adj_list.items():
            print("V", vertex, ":", n)

    def BFS(self, s):
        # Mark all vertices as not visited
        visited = [False] * self.vertex_count
        # Create a queue for BFS
        queue = deque([s])
        # Mark the source node as visited
        visited[s] = True

        while queue:
            # Dequeue a vertex from queue
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent vertex has not been visited, mark it visited and enqueue it
            for neighbor, _ in self.adj_list[current_vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.print_adj_list()
print("BFS starting from vertex 0:")
g.BFS(3)
