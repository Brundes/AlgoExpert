# Iterative Solution
# Notation of time: O(log n)

def findClosestValueInBst(tree, target):

    storage = tree.value

    while tree is not None:
        
        if target > tree.value:
            storage = tree.value
            tree = tree.right
            
        else:
            storage = tree.value
            tree = tree.left

    return storage

    
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Building the BST
root = BST(10)
root.left = BST(5)
root.right = BST(15)
root.left.left = BST(2)
root.left.right = BST(5)
root.right.left = BST(13)
root.right.right = BST(22)
root.left.left.left = BST(1)
root.right.left.right = BST(14)

# Target to find the closest value to
target = 12

# Running the function
result = findClosestValueInBst(root, target)
print("Closest value to", target, "is:", result)