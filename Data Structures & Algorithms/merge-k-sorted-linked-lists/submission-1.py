class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0
        dummy = curr = ListNode()

        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, counter, l))
                counter += 1
        
        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1
        
        return dummy.next