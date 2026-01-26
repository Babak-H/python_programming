# Queue

'''
queue is a data structure similar to stack.
Queues, like the name suggests, follow the First-in-First-Out (FIFO) principle. 
As if waiting in a queue for the movie tickets, the first one to stand in line is the first one to buy a ticket and enjoy the movie.
To implement a queue, therefore, we need two simple operations:

enqueue - adds an element to the end of the queue
dequeue - removes the element at the beginning of the queue
'''

# a "queue" of fruits:
fruits = []

# Let's enqueue some fruits into our list
fruits.append('banana')
fruits.append('grapes')
fruits.append('mango')
fruits.append('orange')

# Now let's dequeue our fruits, we should get 'banana'
first_item = fruits.pop(0)
print(first_item)

# If we dequeue again we'll get 'grapes'
first_item = fruits.pop(0)
print(first_item)

# 'mango' and 'orange' remain
print(fruits)  # ['c', 'a'

# here we use the append and pop operations of the list to simulate the core operations of a queue.
# we create a queue class that uses list object as it's base

# here we create a queue class that uses list object as it's base


class Queue(object):

    def __init__(self):
        self.items = []
        
    # add items to the queue (first position = last element to be peeked or popped)
    def enqueue(self, item):
        self.items.insert(0, item)

    # remove items from queue (remove first item of the queue)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    # view first item in the queue
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return len(self.items)


'''
Queues have widespread uses in programming as well. Think of games like Street Fighter or Super Smash Brothers. 
Players in those games can perform special moves by pressing a combination of buttons. These button combinations can 
be stored in a queue.
Now imagine that you're a developer working on a new fighting game. In your game, every time a button is pressed, an 
input event is fired. A tester noticed that if buttons are pressed too quickly the game only processes the first one 
and special moves won't work!
You can fix that with a queue. We can enqueue all input events as they come in. This way it doesn't matter if input events 
come with little time between them, they'll all be stored and available for processing. When we're processing the moves 
we can dequeue them. A special move can be worked out like this:
'''

input_queue = Queue()

# The player wants to get the upper hand so pressing the right combination of buttons quickly
input_queue.enqueue('DOWN')  
input_queue.enqueue('RIGHT')  
input_queue.enqueue('B')


# Now we can process each item in the queue by dequeueing them
key_pressed = input_queue.dequeue() # 'DOWN'

# We'll probably change our player position
key_pressed = input_queue.dequeue() # 'RIGHT'

# We'll change the player's position again and keep track of a potential special move to perform
key_pressed = input_queue.dequeue() # 'B'

# This can do the act, but the game's logic will know to do with the special move
