INF_DISTANCE = 1e7

class Graph():
    def __init__(self, vertices) -> None:
        self.V = vertices

        self.graph = [[0 for colluymn in range(vertices)]
                      for row in range(vertices)]
        
    def print_solution(self, distance):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", distance[node])

    def find_min_distance_vertex(self, distance, shortest_path_set):
        min = INF_DISTANCE

        for v in range(self.V):
            if distance[v] < min and shortest_path_set[v] is False:
                min = distance[v]
                min_index = v

        return min_index
    
    def dijkstra(self, source):

        distance = [INF_DISTANCE] * self.V
        distance[source] = 0
        shortest_path_set = [False] * self.V

        for _ in range(self.V):
            u = self.find_min_distance_vertex(distance, shortest_path_set)
            shortest_path_set[u] = True

            for v in range(self.V):
                if(self.graph[u][v] > 0 and shortest_path_set[v] is False and
                   distance[v] > distance[u] + self.graph[u][v]):
                    distance[v] = distance[u] + self.graph[u][v]

        self.print_solution(distance)

g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0], 
           [4,0,8,0,0,0,0,11,0], 
           [0,8,0,7,0,4,0,0,2], 
           [0,0,7,0,9,14,0,0,0], 
           [0,0,0,9,0,10,0,0,0], 
           [0,0,4,14,10,0,2,0,0], 
           [0,0,0,0,0,2,0,1,6], 
           [8,11,0,0,0,0,1,0,7], 
           [0,0,2,0,0,0,6,7,0]]

g.dijkstra(0)