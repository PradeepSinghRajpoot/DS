# @Author - Pradeep Singh Rajpoot

def height(node): 
    result = -1
    if node is not None:
        result = node.height
    return result

def updateHeight(node):
    if node is not None:
        node.height = max(height(node.left), height(node.right)) + 1

def balanceFactor(node):
    return (height(node.left) - height(node.right))

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1;

# Credits - Code taken from MIT 6.001 course (thx erik demaine) 
    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.data) 
        #label = str(self.data) + ' (' + str(self.height) + ') bf=' + str( balanceFactor(self)  ) 
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


class AVL:
    def __init__(self):
        self.root = None;

    def insertNode(self, node, root = None):
        if root == None:
            root = self.root

        if self.root == None:
            self.root = node
            root = node
        elif node.data < root.data:
            if root.left  == None:  
                node.parent = root;
                root.left = node
                self.rebalance(node);
            else:
                self.insertNode(node, root.left)
        elif node.data > root.data:
            if root.right == None:
                node.parent = root;
                root.right = node
                self.rebalance(node);
            else:
                self.insertNode(node, root.right)

        updateHeight(node);
        updateHeight(root);


    def rebalance(self, node):
        #print('rebalance-' + str(node.data))
        while node is not None:

            updateHeight(node);

            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.rightRightRotate(node);
                else:
                    self.leftRightRotate(node);
            elif height(node.right) >= 2 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.leftLeftRotate(node);
                else:
                    self.rightLeftRotate(node);

            node = node.parent


    def leftLeftRotate(self, x):
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y

        updateHeight(x);
        updateHeight(y);

    def rightRightRotate(self, x):
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y

        updateHeight(x);
        updateHeight(y);
 

#    def leftLeftRotate(self, node):
#        p = node.right
#        print(p)
#        print(p.data);
#        print(p.left);
#        node.right = p.left
#        p.left = node
#
#        node.height = max(height(node.left), height(node.right)) + 1 
#        p.height = max(height(p.left), node.height) +1 ; 
#
#        return p
#
#    def rightRightRotate(self, node):
#        p = node.left
#        node.left = p.right
#        p.right = node
#
#        node.height = max(height(node.left), height(node.right))  + 1
#        p.height = max(height(p.right), node.height) + 1
# 
#        return p

    def leftRightRotate(self, node):
        self.rightRightRotate(node.left)
        self.leftLeftRotate(node)

    def rightLeftRotate(self, node): 
        self.leftLeftRotate(node.right)
        self.rightRightRotate(node);




tree1 = AVL();
tree1.insertNode(AVLNode(20))
tree1.insertNode(AVLNode(40))
tree1.insertNode(AVLNode(60))
print (tree1.root)
print()

tree1.insertNode(AVLNode(70))
print (tree1.root);
print()

tree1.insertNode(AVLNode(80))
print (tree1.root);
print()



#tree1.preOrderTraversal(tree1.root)


