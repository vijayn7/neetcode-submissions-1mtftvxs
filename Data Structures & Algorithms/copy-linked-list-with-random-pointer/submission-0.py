class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        mapping = {}

        while curr:
            mapping[curr] = Node(curr.val)  # curr.val, not head.val
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                mapping[curr].next = mapping[curr.next]
            if curr.random:
                mapping[curr].random = mapping[curr.random]
            curr = curr.next

        return mapping[head]