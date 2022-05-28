class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Represent the head and tail of the singly linked list  
    def __init__(self):
        self.head = None
        self.tail = None

        # add_node() will add a new node to the list  

    def add_node(self, data):
        # Create a new node  
        new_node = Node(data)

        # Checks if the list is empty  
        if self.head is None:
            # If list is empty, both head and tail will point to new node  
            self.head = new_node
            self.tail = new_node
        else:
            # new_node will be added after tail such that tail's next will point to new_node  
            self.tail.next = new_node
            # new_node will become new tail of the list  
            self.tail = new_node

            # sort_list() will sort nodes of the list in ascending order  

    def sort_list(self):
        # Node current will point to head  
        current = self.head
        index = None

        if self.head == None:
            return
        else:
            while current is not None:
                # Node index will point to node next to current  
                index = current.next

                while index != None:
                    # If current node's data is greater than index's node data, swap the data between them  
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

                # display() will display all the nodes present in the list  

    def display(self):
        # Node current will point to head  
        current = self.head
        if self.head == None:
            print("List is empty")
            return
        while current != None:
            # Prints each node by incrementing pointer  
            print(current.data)
            current = current.next


if __name__ == "__main__":
    sList = LinkedList()

# Adds data to the list  
sList.add_node(9)
sList.add_node(7)
sList.add_node(2)
sList.add_node(5)
sList.add_node(4)

# Displaying original list  
print("Original list: ")
sList.display()

# Sorting list  
sList.sort_list()

# Displaying sorted list  
print("Sorted list: ")
sList.display()
