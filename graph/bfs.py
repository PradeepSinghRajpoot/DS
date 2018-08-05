from graph import Graph 
import queue

def bfs(g, start):

    start.setPred(None)
    start.setDistance(0)

    vertQueue = queue.Queue()
    vertQueue.put(start)

    while (vertQueue.qsize() > 0):
        currentVert = vertQueue.get()
        for nbr in currentVert.getConnections():
            if(nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.put(nbr)

        print (currentVert.getId())
        currentVert.setColor('black')



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
bfs(g,start)  
