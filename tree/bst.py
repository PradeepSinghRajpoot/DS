# @Author - Pradeep Singh Rajpoot

#import jsonpickle # pip install jsonpickle
#import json

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    # Credits - Code taken from MIT 6.001 course (thx erik demaine) 
    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.data)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle-2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
          [left_line + ' ' * (width - left_width - right_width) + right_line
           for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def __str__(self):
        return '\n'.join(self._str()[0])


class BST():
    def __init__(self):
        self.root = None


class BST:
    def __init__(self):
        self.root = None;

    def insertNode(self, node, root = None):
        if root == None:
            root = self.root

        if self.root == None:
            self.root = node
        elif node.data < root.data:
            if root.left  == None:  
                node.parent = root;
                root.left = node
            else:
                self.insertNode(node, root.left)
        elif node.data > root.data:
            if root.right == None:
                node.parent = root;
                root.right = node
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



tree1 = BST();
tree1.insertNode(BSTNode(20))
tree1.insertNode(BSTNode(40))
tree1.insertNode(BSTNode(60))
tree1.insertNode(BSTNode(80))
tree1.insertNode(BSTNode(30))
tree1.insertNode(BSTNode(35))
#tree1.printPreOrder(tree1.root)
print (tree1.root);

#serialized = jsonpickle.encode(tree1)
#print(json.dumps(json.loads(serialized), indent=2))

#tree1.preOrderTraversal(tree1.root)


