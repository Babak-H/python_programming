# Singly Linked Lists

# class for each node of the LinkedList
class Node:
    def __init__(self, data):
        # data and next value for each node
        self.data = data
        # next shows what is the next value of linkedlist
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None  # head is the first element of the linked list


    def append(self, data):
        new_node = Node(data)
        # check if list is empty
        if self.head == None:
            # set the first value as head of the list
            self.head = new_node
            return
        # set the head as last node
        last_node = self.head
        # then loop through all nodes and check their next
        while last_node.next:
            # set last node as next value of current node
            last_node = last_node.next
        # if you finally reach the node that has empty value set the new value as it's next
        last_node.next = new_node


    def print_list(self):
        cur_node = self.head
        # until a node exists, print it's data, get later node from it's next property and print that too
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


    def prepend(self, data):
        new_node = Node(data)
        # first set new_node's next as current head node
        new_node.next = self.head
        # next set new_node as the head node
        self.head = new_node


    def insert_after_node(self, prev_node, data):
        # this will actually check if this object exists in linkedlist:
        if not prev_node:
            print("previous node doesnt exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    # delete node
    # given a key(data field) delete node with this field, assume elemenets in linked list are unique
    # Example : delete node with data field "B"
    def delete_node(self, key):
        cur_node = self.head
        # Node is head of the list : first remove the head pointer from this node, then remove its next value pointer.
        if cur_node and cur_node.data == key:
            # remove head pointer
            self.head = cur_node.next

            #   Setting the variable to None is precisely the same idea as setting the variable to "null" when implementing a
            #   linked list in language like C++ or Java. When implementing these things in C++/Java, you want to make sure that
            #   you do indeed set the nodes to null when they stop pointing to other nodes in the list so as to avoid
            #  "dangling pointers". It's kind of the same idea here, although most likely nothing catastrophic will happen if you
            #  don't, it's just good practice.
            cur_node = None
            return

        # Node to be deleted is not head : connect node that preceds this node to the one that is after 
        # it, then make this node's next value set to empty, then set this node that we want to delete 
        # to None, we also need to find this nodes preceding node
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:  # meabs we didnt find this key
            return

        prev.next = cur_node.next
        cur_node = None


    def del_at_pos(self, idx):
        cur_node = self.head
        if idx == 0:
            self.head = cur_node.next
            cur_node = None
            return 
        
        prev = None
        count = 0
        while cur_node and count != idx:  # loop until you reach the index
            prev = cur_node
            cur_node = cur_node.next
            count += 1
            
        if cur_node is None: # for the case that idx is out of range
            return
        
        prev.next = cur_node.next
        cur_node = None


    # find length of linkedList by looping through each element via next property
    def len_iterative(self):
        count = 0
        cur_node = self.head
        
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count


    # find length in recursive mode, first node that we give as arg should be head of the linked list
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next) 


    # two cases for swap nodes(assuming all elements are unique) :
    # 1- node1 and node2 are not heads  2- either node1 or node2 is head
    def swap_nodes(self, node1, node2):
        if node1 == node2:
            return
        
        # find previous node of the node1, if not it is a head node
        prev_1 = None
        curr_1 = self.head
        # loop through all elements to find the first node to swap
        while curr_1 and curr_1.data != node1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != node2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        
        # if either of these nodes doesnt exist, exit this function
        if not curr_1 or not curr_2:
            return
        
        # if first node has a node before it, then set that node's next to node2
        # otherwise (means node1 is head, set node2 as head)
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
            
        if prev_2:
            prev_2.next = curr_1 
        else:
            self.head = curr_1
        
        # after that, we swap next pointers of node1 and node2
        # a,b = b,a
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    
    # reverse the node so head node becomes the last element
    def reverse_iterative(self):
        prev = None
        # cur is a pointer to the head of list
        cur = self.head
        
        # A->B->C  , what we do here, is reversing previous/next pointer of each of nodes, one by one
        while cur: # cur = B
            temp  = cur.next # temp = C
            cur.next = prev # cur.next = A
            prev = cur # prev = B
            cur = temp # cur = C , so we can traverse the next item of the linkedList
            
        self.head = prev  # self.head = C, since C was last element in original linkedList

    
    def reverse_recursive(self):
        # instead of using while loop we call this inner function recursively
        def _reverse_recursive(cur, prev):  # A, None
            # when you reach end of the list
            if not cur:
                return prev
            # similar to iterative mode
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            return _reverse_recursive(cur=cur, prev=prev)
            
        self.head = _reverse_recursive(cur=self.head, prev=None)

    
    def merge_sorted(self, llist):
        # set p and q pointers to head nodes of list1 and list2 (both of p,q are objects of class Node)
        p = self.head
        q = llist.head
        s = None
        
        # if either of the two lists doesnt exist return out of function (no point of sorting)
        if not p:
             return
        if not q:
             return
        
        # if both head pointers exist:
        if p and q:
            #based on which header data being smaller set s to that one
            if p.data <= q.data:
                s = p
                p = s.next # move p to next element, can also write : p = p.next
            else:
                s = q
                q = s.next # move p to next element, can also write : q = q.next
                
            new_head = s
            
            # go through all elements of both lists (after p/q being updated)
            while p and q:
                if p.data <= q.data:
                    # the p/q here is one item iterated ahead of when we set s = p/q
                    s.next = p
                    # then we move s one item ahead, it its next pointer
                    s = p  # could also write s = s.next
                    p = s.next # could also write p.next, we move p one item ahead
                    
                else:
                    s.next = q
                    s = q # could also write s = s.next
                    q = s.next # could also write q.next, we move q one item ahead
                    
        # when you reach end of the list in one of the lists, set s to whatever is left of the other list and finish merging   
            if not p:
                s.next = q
                
            if not q:
                s.next = p
                
            self.head = new_head


    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()
        
        while cur:
            if cur.data in dup_values:
                # remove duplicate node and set the previous node's next to one after this
                prev.next = cur.next
                cur = None # remove duplicate node
            else:
                # have not encountered element before
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next  # could be written as cur.next

    
    def print_nth_from_last(self, n):
        ## Method 1
        # final total length of the list
        total_len = self.len_iterative()
        
        # then iterate through list, subtracting 1 element each time to reach the nth point, then print it
        cur = self.head
        while cur:
            if total_len == n:
                print(cur.data)
                return cur
            total_len -= 1
            cur = cur.next
        
        if cur is None:
            return 

        ## Method 2
        # put both p,q to zero element
        p = self.head
        q = self.head
        
        # then move q pointer to the nth posititon
        count = 0
        while q and count < n:
            q = q.next
            count += 1

        if not q:
            return
        print(q.data)
        
        # iterate until q reaches null, p reaches n and print p
        while p and q:
            p = p.next
            q = q.next
        return p.data


    def count_occurance_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count+= 1
            cur = cur.next
        return count
    

    def count_occurances_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurances_recursive(node.next, data)
        else:
            return self.count_occurances_recursive(node.next, data)


    # num is not value of the node but the index of the node
    # 1 2 3 4 5 6 --> 5 6 1 2 3 4
    def rotate_list(self, k):
        p = self.head
        q = self.head
        
        prev = None
        count = 0
        # set p to kth element
        while p and count < k:
            prev = p     # prev = 4
            p = p.next   # p = 5
            q = q.next   # q = 5
            count += 1  
        p = prev
        
        # set q to last element of the list
        while q:
            prev = q
            q = q.next
        q = prev
        
        # set next element of current last element to current head
        q.next = self.head
        # then set current head to element after 4
        self.head = p.next
        # then set element of 4 to None
        p.next = None


    def is_palindrome(self):
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
#       if s == s[::-1]:
#           return True
#       return False
        return s == s[::-1]  # if string is equal to itself when reveresed


    # A B C D --> D A B C
    def tail_to_head(self):
        last = self.head
        second_to_last = None
        
        # this way it wont iteratate the last element since it's .next value points to null
        while last.next:
            second_to_last = last
            last = last.next
        
        # set last elements next pointer to current head pointer
        last.next = self.head
        # set the one before it's next pointer to None (to avoid having circular linkedList)
        second_to_last.next = None
        # then set head to last element
        self.head = last

    
    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        sum_list = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10 # or it can be s-10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)
            # since above we checked p OR q , now we need to check if both of them exist:
            if p:    
                p = p.next
            if q:
                q = q.next
        
        sum_list.print_list() 

# ================================

llist = LinkedList()

llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E")

# this is how we retrieve the cell node that we want to add after it
print("node that we want to add after it: " , llist.head.next.data)
llist.insert_after_node(llist.head.next, "F")
llist.print_list()

llist.delete_node("E")
llist.delete_node("B")
print(" ")
llist.print_list()

print(llist.len_iterative(), "iterative")
print(llist.len_recursive(llist.head), "recursive")

print(" ")
llist.print_list()
llist.swap_nodes("F", "C")
print(" ")
llist.print_list()

print(" ")
llist.reverse_iterative()
llist.print_list()

print("")
llist.reverse_recursive()
llist.print_list()


llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()


# if you change copy variable, original one doesn't changes
i = 5
j = i
j = 3
print(i)


# if you change original variable, copy does NOT change
i = 3
j = i
i = 5
print(j)


list_ = LinkedList()
list_.append(1)
list_.append(6)
list_.append(1)
list_.append(4)
list_.append(2)
list_.append(2)
list_.append(4)
list_.print_list()
print("")
list_.remove_duplicates()
list_.print_list()

print("")
print(list_.print_nth_from_last(2))


list_ = LinkedList()
list_.append(1)
list_.append(6)
list_.append(1)
list_.append(4)
list_.append(1)
list_.append(1)

print(list_.count_occurance_iterative(1))
print(list_.count_occurances_recursive(list_.head, 1))

list_.rotate_list(4)  # result should be 1 1 1 6 1 4
list_.print_list()


# RACECAR , RADAR
list_ = LinkedList()
list_.append("R")
list_.append("A")
list_.append("D")
list_.append("A")
list_.append("R")

list_1 = LinkedList()
list_1.append("A")
list_1.append("B")
list_1.append("C")

print(list_.is_palindrome())
print(list_1.is_palindrome())


list_1 = LinkedList()
list_1.append("A")
list_1.append("B")
list_1.append("C")
list_1.append("D")

list_1.print_list()
print(" ")
list_1.tail_to_head()
list_1.print_list()


# 3 6 5 
# 2 4 8 
# ------
#  
llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

llist1.sum_two_lists(llist2)



