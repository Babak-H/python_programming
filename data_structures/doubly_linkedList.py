# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None


    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            # loop until you get to last node, then put the new node in it's next pointer
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next

            cur.next = new_node
            new_node.prev = cur


    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            # replace head node with the new node
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node


    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next


    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            # if the linkedList has only one node
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            # when you find the key node, add new node between the key node and its next node
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
                return
            cur = cur.next


    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            # if key node is head node, then add new node before it
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
                return
            cur = cur.next


    def remove(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # Case 1: list has only one element
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                # Case 2: move head pointer to next element in the list
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    self.head = nxt
                    cur = None
                    return
            # when key is NOT head node
            elif cur.data == key:
                # Case 3: when key isn't first or last node
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    # kill off the pointers that don't do anything
                    cur.prev = None
                    cur.next = None
                    cur = None
                    return
                # Case 4: when key is the last node on the list
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return

            cur = cur.next


    def reverse(self):
        tmp = None
        cur = self.head
        while cur: # A
            # temporary pointer keeps the previous node, then we switch next and prev pointers
            tmp = cur.prev # null
            cur.prev = cur.next  # cur.prev = B
            cur.next = tmp # cur.next = null
            # this mean go to the next node in the list
            cur = cur.prev  # cur = B

        # the reason we have if here is for edge cases when there is 0 or 1 elements in the list
        if tmp: # temp is "C" so its previous items points to "D"
            self.head = tmp.prev


    # here instead of key(data), we are given the node itself
    def remove_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    self.head = nxt
                    cur = None
                    return
            elif cur == node:
                # Case 3:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    # kill of the pointers that don't do anything
                    cur.prev = None
                    cur.next = None
                    cur = None
                    return
                # Case 4:
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return

            cur = cur.next


    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next  # we save next pointer so we know where to go after removing this node
                self.remove_node(cur)
                cur = nxt


    # we give this function a number value, then we need to find the pairs from list that add up to 
    # that value and return them
    def pair_with_sum(self, sum_val):
        pairs = list()
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum_val:
                    pairs.append((p.data, q.data))
                q = q.next
            p = p.next
        return pairs


# ================================

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(0)
dllist.add_after_node(1, 11)
dllist.add_before_node(4, 25)
dllist.print_list()

dllist.remove(0)
dllist.remove(25)
dllist.remove(4)
print(" ")
dllist.print_list()

dllist = DoublyLinkedList()
dllist.append("A")
dllist.append("B")
dllist.append("C")
dllist.append("D")
dllist.reverse()
print(" ")
dllist.print_list()

dllist = DoublyLinkedList()
dllist.append("A")
dllist.append("B")
dllist.append("B")
dllist.append("C")
dllist.append("D")
dllist.append("C")
dllist.remove_duplicates()
print(" ")
dllist.print_list()

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
# (1,2) (1,3) (1,4) (1,5)
# (2,3) (2,4) (2,5)  : don't take any values from 1
# (3,4) (3,5)
# (4,5)
print(dllist.pair_with_sum(5))
print(dllist.pair_with_sum(0))