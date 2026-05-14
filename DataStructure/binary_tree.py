class TreeNode:
    """
    Basic building block of a binary tree.
    Each node has a value and pointers to left and right children.
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node value {self.value}"


class BinaryTree:
    """
    Binary Tree implementation with common traversal and utility methods.

    KEY CONCEPTS FOR INTERVIEWS:
    - DFS (Depth First Search): InOrder, PreOrder, PostOrder
    - BFS (Breadth First Search): Level Order
    - Tree properties: height, size
    - LCA (Lowest Common Ancestor) - very common interview question
    """

    def __init__(self, root=None):
        self.root = root

    def inOrder_traversal(self, node):
        """
        DFS - Depth First Search: Left -> Root -> Right
        """
        if node is None:
            return []
        return (self.inOrder_traversal(node.left) +
                [node.value] +
                self.inOrder_traversal(node.right))

    def preOrder_traversal(self, node):
        """
        DFS - Depth First Search: Root -> Left -> Right
        """
        if node is None:
            return []
        return ([node.value] +
                self.preOrder_traversal(node.left) +
                self.preOrder_traversal(node.right))

    def postOrder_traversal(self, node):
        """
        DFS - Depth First Search: Left -> Right -> Root
        """
        if node is None:
            return []
        return (self.postOrder_traversal(node.left) +
                self.postOrder_traversal(node.right) +
                [node.value])

    def levelOrder_traversal(self, node):
        """
        BFS - Breadth First Search: Level by level (left to right)

        ALGORITHM:
        1. Start with root in queue
        2. While queue not empty:
           - Dequeue node
           - Process node
           - Enqueue left and right children
        """
        if node is None:
            return []

        result = []
        queue = [node]  # Initialize queue with root

        while queue:
            current = queue.pop(0)  # Dequeue from front (FIFO)

            if current is None:
                result.append(None)
            else:
                result.append(current.value)
                queue.append(current.left)  # Enqueue left child
                queue.append(current.right)  # Enqueue right child

        # Remove trailing None values for cleaner output
        while result and result[-1] is None:
            result.pop()
        return result

    def height(self, node):
        """
        Maximum depth/height of the tree.

        FORMULA: height = 1 + max(left_height, right_height)

        TIP: Height = number of edges on longest path from root to leaf + 1
        """
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def size(self, node):
        """
        Total number of nodes in the tree.

        FORMULA: size = 1 (current) + size(left) + size(right)

        TIP: Simple recursive counting - good warmup question
        """
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def find_LeastCommonAncestor(self, node: 'TreeNode', val1, val2):
        """
        Find Lowest Common Ancestor (LCA) of two nodes.

        ⭐ VERY COMMON INTERVIEW QUESTION ⭐

        INTERVIEW NOTES:
        - Time Complexity: O(n) - might visit all nodes
        - Space Complexity: O(h) - recursion depth

        ALGORITHM:
        1. Base case: If node is None, return None
        2. If current node matches val1 or val2, return current node
        3. Recursively search left and right subtrees
        4. If both subtrees return non-None, current node is LCA
        5. Otherwise, return whichever subtree found a match

        KEY INSIGHT:
        - If val1 is in left subtree and val2 is in right subtree,
          current node is their LCA
        - If both are in same subtree, LCA is deeper in that subtree

        VARIATIONS TO PRACTICE:
        - LCA in BST (can use value comparisons for O(h) solution)
        - LCA with parent pointers
        - LCA for multiple nodes

        EXAMPLE from tree in main:
        - LCA(3, 9) = 8 (both in left subtree)
        - LCA(3, 13) = 10 (different subtrees, root is LCA)
        """
        # Base case: reached leaf or found one of the target nodes
        if node is None:
            return None

        # If current node is one of the targets, it's potentially the LCA
        if node.value == val1 or node.value == val2:
            return node

        # Recursively search both subtrees
        left_node = self.find_LeastCommonAncestor(node.left, val1, val2)
        right_node = self.find_LeastCommonAncestor(node.right, val1, val2)

        # If targets found in different subtrees, current node is LCA
        if left_node and right_node:
            return node

        # Otherwise, return whichever subtree has the targets
        # (both targets are in same subtree)
        return left_node if left_node else right_node

    def build_from_levelorder(self, values):
        """
        Reconstruct binary tree from level-order array representation.
        None represents missing nodes.

        INTERVIEW NOTES:
        - Time Complexity: O(n)
        - Space Complexity: O(n) for queue

        Example: [10, 8, 12, 3, 9, None, 13]
        Creates:
                 10
                /  \
               8    12
              / \     \
             3   9     13

        ALGORITHM:
        1. First value is root
        2. Use queue to track parent nodes
        3. For each parent, assign next two values as left/right children
        4. Add non-None children to queue to become parents
        5. Continue until all values processed

        COMMON QUESTIONS:
        - "Deserialize a tree"
        - "Build tree from array representation"
        - Opposite of level-order traversal

        TIP: This is how LeetCode represents trees in test cases!
        Understanding this helps visualize problems.
        """
        if not values or values[0] is None:
            return None

        # Create root node from first value
        root = TreeNode(values[0])
        queue = [root]  # Queue of parent nodes
        i = 1  # Index for values array

        while queue and i < len(values):
            current = queue.pop(0)  # Get next parent

            # Assign left child
            if i < len(values):
                if values[i] is not None:
                    current.left = TreeNode(values[i])
                    queue.append(current.left)  # Add to queue as future parent
                i += 1

            # Assign right child
            if i < len(values):
                if values[i] is not None:
                    current.right = TreeNode(values[i])
                    queue.append(current.right)  # Add to queue as future parent
                i += 1

        return root

    def print_tree(self, node, level=0, prefix="Root: "):
        """
        Visual tree representation for debugging/understanding.

        INTERVIEW NOTES:
        - Not typically asked in interviews
        - Extremely useful for debugging and visualizing
        - Shows tree structure with indentation

        TIP: Use this to verify your tree construction is correct!
        """
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")

                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


if __name__ == "__main__":
    """
    Example tree construction and testing all methods.

    TREE STRUCTURE:
           10(A)
          /     \
        8(B)    12(C)
       /   \         \
      3(D) 9(E)     13(F)

    INTERVIEW TIP:
    Always draw the tree structure when solving problems!
    It helps visualize the solution.
    """

    # Manual tree construction (Method 1)
    A = TreeNode(10)
    B = TreeNode(8)
    C = TreeNode(12)
    D = TreeNode(3)
    E = TreeNode(9)
    F = TreeNode(13)

    A.left = B
    A.right = C

    B.left = D
    B.right = E

    C.right = F

    tree = BinaryTree(A)

    # Print visual representation
    print("TREE STRUCTURE:")
    tree.print_tree(tree.root)
    print()

    # Test all traversal methods
    print("TRAVERSAL METHODS:")
    print(f"DFS - InOrder:   {tree.inOrder_traversal(tree.root)}")  # [3, 8, 9, 10, 12, 13]
    print(f"DFS - PreOrder:  {tree.preOrder_traversal(tree.root)}")  # [10, 8, 3, 9, 12, 13]
    print(f"DFS - PostOrder: {tree.postOrder_traversal(tree.root)}")  # [3, 9, 8, 13, 12, 10]
    print()

    # Test BFS
    print(f"BFS - Level by level: {tree.levelOrder_traversal(tree.root)}")  # [10, 8, 12, 3, 9, None, 13]
    print()

    # Test utility methods
    print("TREE PROPERTIES:")
    print(f"Height: {tree.height(tree.root)}")  # 3
    print(f"Size:   {tree.size(tree.root)}")  # 6
    print()

    # Test LCA (common interview question!)
    print("LOWEST COMMON ANCESTOR (LCA):")
    val1, val2 = 3, 13
    lca = tree.find_LeastCommonAncestor(tree.root, val1, val2)
    print(f"LCA({val1}, {val2}): {lca}")  # Node value 10

    val1, val2 = 3, 9
    lca = tree.find_LeastCommonAncestor(tree.root, val1, val2)
    print(f"LCA({val1}, {val2}): {lca}")  # Node value 8