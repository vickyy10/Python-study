

class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data
        self.next = None  # Initialize the next pointer to None

class SinglyLinkedList:

    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head = new_node

        print(new_node)




sll = SinglyLinkedList()

sll.insert_at_beginning(0)

sll.print_list()