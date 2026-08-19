# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        st = [(root, 0)]

        while st:
            curr = st.pop()

            if not curr[0]:
                continue

            if len(res) < curr[1] + 1:
                res.append(curr[0].val)

            if curr[0].left:
                st.append((curr[0].left, curr[1] + 1))
            
            if curr[0].right:
                st.append((curr[0].right, curr[1] + 1))
        
        return res