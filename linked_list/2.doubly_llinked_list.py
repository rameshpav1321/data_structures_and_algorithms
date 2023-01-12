class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def push_front(self,node):
        if self.head:
            self.head.prev=node
            node.next=self.head
            self.head=node
        else:
            self.head=node
    def reverse_dllist(self):
        if self.head:
            curr_node=self.head
            while curr_node!=None:
                if curr_node.next==None:
                    self.head=curr_node
                curr_node.prev,curr_node.next=curr_node.next,curr_node.prev
                curr_node=curr_node.prev             
        else:
            return "Referenced non existing list"
    def del_head(self):
        if self.head:
            if self.head.next==None:
                self.head=None
            else:
                self.head=self.head.next
                self.head.prev=None
        else:
            return
    def del_tail(self):
        if self.head:
            if self.head.next==None:
                self.head=None
            else:
                curr_node=self.head
                while curr_node.next!=None:
                    curr_node=curr_node.next
                curr_node.prev.next=None
        else:
            return
    
    def print_dllist(self):
        temp_node=self.head
        while temp_node!=None:
            print(temp_node.data,end='->')
            temp_node=temp_node.next
        print('Null')

if __name__=="__main__":
    dllist=DoublyLinkedList()
    dllist.push_front(Node(1))
    dllist.push_front(Node(2))
    dllist.push_front(Node(3))
    dllist.print_dllist()
    dllist.reverse_dllist()
    dllist.print_dllist()