
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        """Helper function to print the linked list"""
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    out_list = []
    
    while True:
        if l1 == None and l2 == None:
            break

        if l1 == None and l2 != None:
            l1 = ListNode(0)
        if l2 == None and l1 != None:
            l2 = ListNode(0)

        val = l1.val + l2.val
        if val >= 10:
            t_place = val // 10
            val = val % 10
            if l1.next == None:
                l1.next = ListNode(t_place)
            else:
                l1.next.val = l1.next.val + t_place 
    
        out_list.append(val)
        l1 = l1.next
        l2 = l2.next

    output = None
    for i, out in enumerate(reversed(out_list)):
        if i == 0:
            output = ListNode(out)
            continue

        current_node = ListNode(out)
        current_node.next = output

        output = current_node
    
    return output
    
    
 
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)   


addTwoNumbers(l1, l2)

l1 = ListNode(0)

l2 = ListNode(0)


addTwoNumbers(l1, l2)

prev_node = None
arr = [9,9,9,9,9,9,9]
for n in arr:
    if prev_node == None:
        prev_node = ListNode(n)
        continue
    curr = ListNode(n)
    curr.next = prev_node
    prev_node = curr

l1 = prev_node

prev_node = None
arr = [9,9,9,9]
for n in arr:
    if prev_node == None:
        prev_node = ListNode(n)
        continue
    curr = ListNode(n)
    curr.next = prev_node
    prev_node = curr

l2 = prev_node
addTwoNumbers(l1, l2)

"""
    [1,1,1,1,1,1,1,1]   - 1 i mente.
    ------------------
    [9,9,9,9,9,9,9]
    [9,9,9,9]
    ------------------
    [8,9,9,9,0,0,0,1]


"""
