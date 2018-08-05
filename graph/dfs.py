from graph import Graph 

#time = 0

def dfs(g, start):

    start.setPred(None)
    start.setDistance(0)

    for nbr in start.getConnections():
        if(nbr.getColor() == 'white'):
            dfsvisit(nbr)


def dfsvisit(startVertex):
    startVertex.setColor('gray')
    #time += 1

    #startVertex.setDiscoveryTime(time)
    
    for nextVertex in startVertex.getConnections():
        if (nextVertex.getColor() == 'white'):
            nextVertex.setPred(startVertex)
            dfsvisit(nextVertex)
        
    startVertex.setColor('black')
    #time += 1
    #startVertex.setFinishTime(time)
    print(startVertex.getId())


g = Graph()
for i in range(6):
    g.addVertex(i)

g.vertList

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

start = g.getVertex(2)
dfs(g,start)  
