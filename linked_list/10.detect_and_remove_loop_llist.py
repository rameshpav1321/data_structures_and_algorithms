def detect_and_remove_loop(head):
    slow_pointer=head
    fast_pointer=head
    while fast_pointer and fast_pointer.next:
        slow_pointer=slow_pointer.next
        fast_pointer=fast_pointer.next.next
        if slow_pointer==fast_pointer:
            print('loop detected')
            break
        else:
            return "no loop detected"
        slow_pointer=head
        while slow_pointer.next!=fast_pointer.next:
            slow_pointer=slow_pointer.next
            fast_pointer=fast_pointer.next
        fast_pointer.next=None
        print('loop removed')
    return
    