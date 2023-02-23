def reverse_queue(q,reversed_q):
    if not q:
        return
    val=q.pop(0)
    reverse_queue(q,reversed_q)
    reversed_q.append(val)
    return reversed_q


print(reverse_queue([12,5,15,20],[]))

