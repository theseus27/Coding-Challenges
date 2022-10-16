class Solution:
    def build(self, idx, nodes):
        if not nodes[idx].left and not nodes[idx].right: return nodes
        
        if (nodes[idx].right):
            nodes.insert(idx+1, nodes[idx].right)
            self.build(idx+1, nodes)
        if (nodes[idx].left):
            nodes.insert(idx, nodes[idx].left)
            self.build(idx, nodes)
            
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes: Optional[TreeNode] = [root]
        self.build(0, nodes)
        return nodes[k-1].val