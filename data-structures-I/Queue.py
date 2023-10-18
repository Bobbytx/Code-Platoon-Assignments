####API####
# enqueue - add item to beginning
# dequeue - remove and return item from end
# peek - return last item
# size - return number of items
# is_empty - True if no items, False otherwise
class Queue:
    def __init__(self):
        self.queue_list = []

    def enqueue(self, item):
        self.queue_list.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue_list.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue_list[-1]
    
    def size(self):
        return len(self.queue_list)
    
    def is_empty(self):
        return len(self.queue_list) == 0
    


cust_q = Queue()
cust_q.enqueue("Bobby")

print(f'Testing peek after enqueue for Bobby: {cust_q.peek()}')

cust_q.enqueue("Anya")
cust_q.enqueue("Steph")

print(f"List of customers: {cust_q.queue_list}")
print(f'Testing size (3): {cust_q.size()}')
cust_q.dequeue()
print(f"List of customers: {cust_q.queue_list}")
cust_q.dequeue()
cust_q.dequeue()
cust_q.dequeue() #testing if dequeue is ran on empty list
print(f"List of customers: {cust_q.queue_list}")