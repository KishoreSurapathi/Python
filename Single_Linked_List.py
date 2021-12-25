class node:
    def __init__(self, data=None, nextnode=None):
        self.data = data
        self.nextnode = nextnode

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            newnode = node(data)
            self.head = newnode
        else:
            newnode = node(data)
            newnode.nextnode = self.head
            self.head = newnode

    def insert_at_end(self,data):
        if self.head is None:
            newnode = node(data)
            self.head = newnode
        else:
            newnode = node(data)
            curr = self.head
            while curr.nextnode is not None:
                curr = curr.nextnode
            curr.nextnode = newnode

    def display(self):
        curr = self.head
        llliststr=''
        while curr is not None:
            llliststr = llliststr + str(curr.data) + '----->'
            curr = curr.nextnode
        print(llliststr + ' None')

if __name__ == '__main__':
    llist = LinkedList()

    for i in range(10):
        data = i
        llist.insert_at_beginning(data)

    for i in range(10):
        data = i
        llist.insert_at_end(data)

    llist.display()




