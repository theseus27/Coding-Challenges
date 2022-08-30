#BINARY TREES
    #Index, Search, Insert, Remove all avg O(log n)
    #In-Order Traversal: Left -> Root -> Right
    #Pre-Order Traversal: Root -> Left -> Right
    #Post-Order Traversal: Left -> Right -> Root

#Use node and tree classes
class Node:
    def __init__(self, value):
        #These are instance attributes
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        if self.value:
            if value < self.value:
                if not self.left:       self.left = Node(value)
                else:                   self.left.insert(value)
            elif value > self.value:
                if not self.right:      self.right = Node(value)
                else:                   self.right.insert(value)
        else:
            self.value = value

    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print(self.value, end=" ")
        if self.right:
            self.right.InOrder()

    def PreOrder(self):
        print(self.value, end=" ")
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()
            
    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.value, end=" ")
                  
root = Node(10)
root.insert(2)
root.insert(5)
root.insert(12)
root.insert(7)
root.InOrder()      # = 2 5 7 10 12
print("\n")
root.PreOrder()     # = 10 2 5 7 12
print("\n")
root.PostOrder()    # = 7 5 2 12 10