####API####
# insert - add node to beginning (or end)
# search - find and return a given node
# remove - remove a given node
# size - return number of nodes
# is_empty - True if no nodes, False otherwise

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f'{self.value}'

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        old_node = self.head
        self.head = new_node
        self.head.next = old_node

    def search(self, value):
        current_node = self.head
        while(current_node is not None):
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        return None
        

    def remove(self, value):
        pass

    def size(self):
        pass

    def is_empty():
        pass

    def print_all_items_in_list(self):
        current_node = self.head
        while(current_node is not None):
            print(current_node)
            current_node = current_node.next

my_list = LinkedList()

# Insert values into the linked list
my_list.insert(5)
my_list.insert(10)
my_list.insert(15)

# Search for a value
result = my_list.search(15)

# Print the result
if result:
    print(f"Node with value {result.value} found.")
else:
    print("Node not found.")