# A function to print the color configuration.
def printConfiguration(colors):
    print("The assigned colors are as follows:")
    for i in range(4):
        print("Vertex: ",
              i, " Color: ", colors[i])


'''A function that will check if the current 
colors of the graph is safe or not.'''
def isSafe(graph, colors):
    for i in range(4):
        for j in range(i + 1, 4):
            if (graph[i][j] and colors[j] == colors[i]):
                return False
    return True


'''A recursive function that takes the current index,
number of vertices, and the color array.
If the recursive call returns true then 
the coloring is possible. It returns
false if the m colors cannot be assigned.'''
def ColorGraph(graph, m, i, colors):
    # If we have reached the last vertex 
    #then check and print the configuration.
    if (i == 4):
        if (isSafe(graph, colors)):
            printConfiguration(colors)
            return True
        return False

    # Assigning color to the vertex and 
    #recursively calling the function.
    for j in range(1, m + 1):
        colors[i] = j
        if (ColorGraph(graph, m, i + 1, colors)):
            return True
        colors[i] = 0
    return False


#DRIVER CODE
#Graph representation using adjacency matrix
graph = [[0, 1, 0, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 0],
         [1, 0, 1, 0]]

#Number of colors
m = 3

# Initially the color list is initialized with 0.
colors = [0 for i in range(4)]

#function call
ColorGraph(graph, m, 0, colors)