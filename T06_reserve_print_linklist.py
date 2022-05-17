class ListNode(object):
    def __init__(self, item, _next=None):
        self.item = item
        self._next = _next

    @property
    def next(self):
        return self._next


rp = []


def reserve_print(self, head: ListNode):
    while head:
        rp.append(head.item)
        head = head.next
    return rp[::-1]
