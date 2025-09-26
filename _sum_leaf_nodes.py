
def sum_leaf_nodes(root):
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        return root.value
    return sum_leaf_nodes(root.left) + sum_leaf_nodes(root.right)


# Example usage:
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Create a sample tree: 
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(sum_leaf_nodes(root))  # Output: 12 (4 + 5 + 3)