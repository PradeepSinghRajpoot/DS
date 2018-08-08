from graph import Graph 

#time = 0

def detect_cycle(startVertex):

    #print(startVertex.getId())
    print (str(startVertex.getId()) + ' ' + startVertex.getColor())
    startVertex.setColor('gray')
    #time += 1

    #startVertex.setDiscoveryTime(time)
    
    for nextVertex in startVertex.getConnections():
        if (nextVertex.getColor() == 'white'):
            nextVertex.setPred(startVertex)
            detect_cycle(nextVertex)
        elif (nextVertex.getColor() == 'gray'):
            print ('Cycle detected at vertex ' + str(nextVertex.getId()))
            return 

    startVertex.setColor('black')

    #time += 1
    #startVertex.setFinishTime(time)




g = Graph()
for i in range(6):
    g.addVertex(i)

g.vertList

#Cycle Data
g.addEdge(1,2,5)
g.addEdge(1,3,2)
g.addEdge(2,3,4)
g.addEdge(4,1,9)
g.addEdge(4,5,7)
g.addEdge(5,6,3)
g.addEdge(6,4,1)

start = g.getVertex(1)

detect_cycle(start)  
