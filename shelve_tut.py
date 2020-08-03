import shelve

""" 
shelve: persistent storage of arbitrary python objects. use it when using a relational database is an overkill.
the shelf is accessed by keys, like a dictionary.
the values inside each shelf are pickled (encrypted) and saved in a database using 'dbm' module
"""

s = shelve.open('test_shelf.db')
try:
    s['key1'] = {'int': 10, 'float': 9.5, 'string': 'Sample Data'}  # becomes encrypted
finally:
    s.close()

# to access data again, open the shelf and use it like a dict
s = shelve.open("test_shelf.db")
try:
    existing = s['key1']
finally:
    s.close()

print(existing)

# dbm module doesn't allow several applications writing to same db at same time.
