# Binary Search Tree (BST)

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)


    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:  # recursively go one level deeper
                self._insert(data, cur_node.left)

        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else: # recursively go one level deeper
                self._insert(data, cur_node.right)
        else:
            print("no duplicates allowed")


    def find(self, data):  # returns True/False based on if the value is found or not
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            else: # when _find() returns None value
                return False
        else:
            return None


    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data == cur_node.data:
            return True
        # if the function doesnt find anything it will return None


    def check_bst(self):
        if self.root:
            is_satisfied = self._is_bst_satisfied(self.root, self.root.data)

            if is_satisfied is None:  # if the variable is False, means we didn't find any violation
                return True
            return False
        # if there is no node in the tree, it also satisfies the bst
        return True


    # if we run a correct BST through an inorder_traversal the numbers should go in an ascending order.
    def _is_bst_satisfied(self, cur_node, data):
        if cur_node.left:
            # make a recursive call since there is no violation
            if data > cur_node.left.data:
                return self._is_bst_satisfied(cur_node.left, cur_node.left.data)
            else:
                return False
        if cur_node.right:
            if data < cur_node.right.data:
                return self._is_bst_satisfied(cur_node.right, cur_node.right.data)
            else:
                return False

# ==============================
bst = BST()
# we just use the insert function, and the class decides where to put the new node
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(11)

print(bst.find(3))
print(bst.find(12))

tree = BST()
tree.root = Node(1)
tree.root.left = Node(2)  # problem
tree.root.right = Node(3)

print(bst.check_bst())
print(tree.check_bst())

