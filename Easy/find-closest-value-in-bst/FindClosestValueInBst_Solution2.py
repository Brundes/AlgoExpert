# Recursively Solution
# Notation of time: O(log n)

def findClosestValueInBst(tree, target):
    return findClosestValueHelper(tree, target, tree.value) 

def findClosestValueHelper(tree, target, closest):
    if tree is None:
        return closest

    if abs(target - tree.value) < abs(target - closest):
        closest = tree.value

    if target < tree.value:
        return findClosestValueHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueHelper(tree.right, target, closest)
    else:
        return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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