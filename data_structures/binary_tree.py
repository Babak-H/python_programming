# Binary Tree
'''
a binary tree is a data structure that each node has at most two children, which are reffered to as 
left child and right child.
'''

'''
Binary Tree traversal
Tree traversal : process of of visiting(checking / updating) each node in a tree data structure, exactly 
once. unlike linked lists, canonically traversed in linear order, trees maybe traversed in mutiple ways. 
They maybe traversed in depth-first or breadth-first order. There are 3 common ways to traverse them in depth first order, 
in-order, pre-order, post-order.
'''

# each element of the binary tree is a node
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
        
    def __len__(self):
        return len(self.items)


class Stack(object):
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def __len__(self):
        return len(self.items)


class BinaryTree(object):

    # root is the value that we will feed the first Node
    def __init__(self, root):
        self.root = Node(root)

    # start: is the node that is gonna be updated on every recursive call
    # traversal: string that is gonna be printed to the screen
    # Root -> left -> right
    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    
    # left -> Root -> right
    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal


    def postorder_traversal(self, start, traversal):
        # left -> right -> Root
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


    # Level-order Traversal
    def levelorder_traverse(self, start):
        # return if there is no start point
        if start is None:
            return
        # create a queue and add the start point (root of tree) to queue
        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        # until length of queue is bigger than zero contnue:
        while len(queue) > 0:
            # add value of first element to string then pop it from the queue
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            
            # next add left and right element of the root node to the queue and go to the next round
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        # at end return the string      
        return traversal

    
    # here the difference is that first we add the item to stack, then we empty the stack and print value of each node
    def reverse_levelorder_traversal(self, start):
        if start is None:
            return
        
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        
        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal

    
    # how many branches the tree goes down
    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)

    # size of a binary tree is the number of leafs (including root) that exist on the tree
    def size(self, node):
        if node is None:
            return 0

        queue = Queue()
        queue.enqueue(node)
        count = 0
        while len(queue) > 0:
            count += 1
            node = queue.dequeue()
            # next add left and right element of the root node to the queue and go to the next round
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
      
        return count


    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_traversal(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_traversal(self.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_traverse(self.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_traversal(self.root)
        else:
            pass
    
# =====================

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree("reverse_levelorder"))

print(tree.height(tree.root))
print(tree.size(tree.root))
    