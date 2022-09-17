class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def add_node(self,node,position=None):
        if position==1:
            if self.head:
                curr_head=self.head
                self.head=node
                self.head.next=curr_head
            else:
                self.head=node
        elif position==None:
            if self.head:
                curr_node=self.head
                while curr_node.next!=None:
                    curr_node=curr_node.next
                curr_node.next=node
            else:
                self.head=node
        else:
            curr_position=1
            curr_node=self.head
            while curr_position<position:
                curr_position+=1
                if curr_position==position-1:
                    node.next=curr_node.next
                    curr_node.next=node
    def delete_node(self,key=None):
        if key<1 or self.head==None:
            return
        curr_node=self.head
        if curr_node.data==key:
            self.head=curr_node.next
        else:
            while curr_node.data!=key:
                temp_node=curr_node
                curr_node=curr_node.next
            if curr_node.next:
                temp_node.next=curr_node.next
            else:
                temp_node.next=None
    def print_llist(self):
        temp_node=self.head
        while temp_node!=None:
            print(temp_node.data,end='->')
            temp_node=temp_node.next
        print('Null')
    def search_node(self,key):
        position=1
        if self.head:
            curr_node=self.head
        else:
            return -1
        if curr_node.data==key:
            return position
        while curr_node.data!=key and curr_node.next!=None:
            curr_node=curr_node.next
            position+=1
        return -1

if __name__=="__main__":
    llist=LinkedList()
    llist.add_node(Node(1))
    llist.add_node(Node(2))
    llist.add_node(Node(3))
    llist.add_node(Node(4))
    llist.add_node(Node(5))
    llist.add_node(Node(6))
    llist.add_node(Node(7))
    llist.add_node(Node(8))
    llist.delete_node(5)
    llist.print_llist()
    print(llist.search_node(9))
    
