class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = [[0,1,0,0,0,0,0],
                      [0,0,1,1,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,0,0,1,1],
                      [0,0,1,0,0,0,0],
                      [0,0,1,0,0,0,0],
                      [1,0,0,0,0,1,0]]
    def add_vertex(self):
        for v in range(len(self.edges)):
            self.edges[v].append(0)
        self.vertices.append([0] * (len(self.edges) + 1))
    
    def print_matrix(self):
        print(self.edges)

g = Graph()

g.print_matrix()

print("------")

g.add_vertex()

g.print_matrix()