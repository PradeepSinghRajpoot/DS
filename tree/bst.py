# @Author - Pradeep Singh Rajpoot

#import jsonpickle # pip install jsonpickle
#import json

class BSTNode:
    def __init__(self, data):
        self.data = data;
        self.left = None;
        self.right = None;

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None;

    def insertNode(self, node, root = None):
        if root == None:
            root = self.root

        if self.root == None:
            print(node.data)
            self.root = node
        elif node.data < root.data:
            if root.left  == None:
                root.left = node
                print(node.data)
            else:
                self.insertNode(node, root.left)
        elif node.data > root.data:
            if root.right == None:
                root.right = node
                print(node.data)
            else:
                self.insertNode(node, root.right)


    #def findNode(self, data):

    def printPreOrder(self, node=None):
        if node == None:
            return
        print (node.data, end=' ')
        self.printPreOrder(node.left);
        self.printPreOrder(node.right);


    def printInOrder(self, node=None):
        if node == None:
            return
        self.printInOrder(node.left);
        print (node.data, end=' ')
        self.printInOrder(node.right);


    def printPostOrder(self, node=None):
        if node == None:
            return
        self.printPostOrder(node.left);
        self.printPostOrder(node.right);
        print (node.data, end=' ')


    def printTree(self):
        print('-'*20);
        current_level = [self.root]
        while current_level:
            print(' '.join(str(node) for node in current_level))
            next_level = list()
            for n in current_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
                current_level = next_level






tree1 = BST();
tree1.insertNode(BSTNode(20))
tree1.insertNode(BSTNode(40))
tree1.insertNode(BSTNode(10))
tree1.insertNode(BSTNode(12))
tree1.insertNode(BSTNode(21))
tree1.insertNode(BSTNode(30))
tree1.printPreOrder(tree1.root)
print ();

#serialized = jsonpickle.encode(tree1)
#print(json.dumps(json.loads(serialized), indent=2))

#tree1.preOrderTraversal(tree1.root)


