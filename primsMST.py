class Graph:
    def __init__(self, nodes):
        self.node_count = nodes
        # Initialize the adjacency matrix with zeros
        self.graph = [[0 for column in range(nodes)] 
                    for row in range(nodes)]

    def add_edge(self, node1, node2, weight):
        self.graph[node1][node2] = weight
        self.graph[node2][node1] = weight
        
    def prims_algo(self):
        # Defining a really big number, that'll always be the highest weight in comparisons
        postitive_inf = float('inf')
    
        # This is a list showing which nodes are already selected 
        # so we don't pick the same node twice and we can actually know when stop looking
        selected_nodes = [False for node in range(self.node_count)]
    
        # Matrix of the resulting MST
        result = [[0 for column in range(self.node_count)] 
                    for row in range(self.node_count)]
        
        indx = 0
        # While there are nodes that are not included in the MST, keep looking:
        while(False in selected_nodes):
            # We use the big number we created before as the possible minimum weight
            minimum = postitive_inf
    
            # The starting node
            start = 0
            # The ending node
            end = 0
            for i in range(self.node_count):
                # If the node is part of the MST, look its relationships
                if selected_nodes[i]:
                    for j in range(self.node_count):
                        # If the analyzed node have a path to the ending node AND its not included in the MST (to avoid cycles)
                        if (not selected_nodes[j] and self.graph[i][j]>0):  
                            # If the weight path analized is less than the minimum of the MST
                            if self.graph[i][j] < minimum:
                                # Defines the new minimum weight, the starting vertex and the ending vertex
                                minimum = self.graph[i][j]
                                start, end = i, j
            
            # Since we added the ending vertex to the MST, it's already selected:
            selected_nodes[end] = True
    
            # Filling the MST Adjacency Matrix fields:
            result[start][end] = minimum
            
            if minimum == postitive_inf:
                result[start][end] = 0

            indx += 1
            
            result[end][start] = result[start][end]

        return result

        # Print the resulting MST
        # for node1, node2, weight in result:
    def printMST(self, result):
        MST_weight = 0
        print("EDGES \tWEIGHT")
        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: \t %d" % (i, j, result[i][j]))

                MST_weight += result[i][j]
        print("\nThe weight of MST:", MST_weight)



    
                
#DRIVER CODE                    
# Example graph has 9 nodes
g = Graph(7)
#input form = (node1, node2, weight)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 4)
g.add_edge(0, 5, 5)
g.add_edge(1, 2, 7)
g.add_edge(1, 3, 1)
g.add_edge(1, 5, 8)
g.add_edge(1, 6, 4)
g.add_edge(2, 6, 6)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 2)
g.add_edge(5, 6, 1)

r = g.prims_algo()
g.printMST(r)