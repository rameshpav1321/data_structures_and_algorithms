def insert_in_sorted_llist(llist,val):
    if llist.head:
        new_node=Node(val)
        if val<llist.head.data:
            new_node.next=self.head
            self.head=new_node
        curr_node=self.head
        while curr_node.data>val:
            tmp_node=curr_node
            curr_node=curr_node.next
        new_node.next=curr_node
        tmp_node.next=new_node