def recurse(self, root, k, children):
    if children == k: 
        return (True, root)
    elif root.left != None: 
        return self.recurse(root.left, k, children+1)
    return (False, root)
        
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    smallest = False
    prev = None
    while smallest==False:
        prev = root
        smallest, root = self.recurse(root, k, 0)
    
    return prev.val