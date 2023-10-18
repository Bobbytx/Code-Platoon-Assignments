####API####
# push - add item to top
# pop - remove and return item from top
# peek - return top item
# size - return number of items
# is_empty - True if no items, False otherwise
class Stack:

    def __init__(self):
        self.base = []

    def push(self, item):
        self.base.append(item)

    def pop(self):
        return self.base.pop()

    def peek(self):
        return self.base[-1]

    def size(self):
        return len(self.base)

    def is_empty(self):
        return len(self.base) == 0


def reversed_string(input_str):
    my_stack = Stack()

    for char in input_str:
        my_stack.push(char)
    print(f'chars pushed to list: {my_stack.base}') #print to test chars were appended to list

    print("Top element before reversal:", my_stack.peek())
    rev_str = "" #create string to collect reversed letters
    while not my_stack.is_empty(): #while not empty
        print(f'Letter added to str: {my_stack.peek()}')
        rev_str += my_stack.pop() #concatenate last char in list to str
    return rev_str

print(reversed_string("Bobby"))
