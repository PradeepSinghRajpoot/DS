# @Author - Pradeep Singh Rajpoot
 

class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data;

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

    def printNode(self):
        print(self.data)


class linkedList:

    def __init__(self, head = None):
        self.length = 0;
        self.head = head

    def addNode(self, node):
        if self.length == 0:
            self.addBeg(node)
        else:
            self.addLast(node)


    def addBeg(self, node):
        node.next = self.head
        self.head = node
        self.length = self.length + 1


    def addLast(self, node):
   
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next

        currentNode.next = node
        node.next = None;
        self.length = self.length + 1


    def addAfterValue(self, data, node):

        currentNode = self.head
        while currentNode.next != None:
            if currentNode.data == data :
                break
            else:
                currentNode = currentNode.next


        if currentNode.data == data:
            node.next = currentNode.next
            currentNode.next = node
            self.length += 1;
        else:
            print ("Unable to find data")


    #def addAtPos(self, pos, node):

    #def deleteBeg(self):

    #def deleteLast(self):

    #def deleteValue(self, data):

    #def deleteAtPos(self, pos):

    #def getLength(self):

    #def getFirst(self):

    #def getLast(self):

    #def getAtPos(self, pos):


    def printList(self):
        nodeList = [];
        if self.head != None :
            #print(self.head.data, self.head.next);
            #print(self.head.next.data, self.head.next.next);
            currentNode = self.head
            while currentNode != None :
                nodeList.append(currentNode.data)
                currentNode = currentNode.next

        
        print(nodeList, self.length)


ll = linkedList()
ll.printList()

ll.addNode(Node(1))
ll.printList()

ll.addNode(Node(5))
ll.printList()

ll.addNode(Node(8))
ll.printList()

ll.addNode(Node(50))
ll.printList()

ll.addNode(Node(100))
ll.printList()

ll.addAfterValue(50, Node(75))
ll.printList()


