class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def minDistance(self, dist, sptSet):
        min = float('inf')
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


# Taking user input for the number of vertices
V = int(input("Enter the number of vertices: "))
g = Graph(V)

# Taking user input for the adjacency matrix representation of the graph
print("Enter the adjacency matrix (separate elements with space):")
for i in range(V):
    g.graph[i] = list(map(int, input().split()))

# Taking user input for the source vertex
src = int(input("Enter the source vertex: "))

# Running Dijkstra's algorithm
g.dijkstra(src)

# Sample OP
# Enter the number of vertices: 4
# Enter the adjacency matrix (separate elements with space):
# 0 5 4 0
# 0 0 0 8
# 0 0 0 3
# 0 0 0 0
# Enter the source vertex: 0
# Vertex   Distance from Source
# 0                0
# 1                5
# 2                4
# 3                7