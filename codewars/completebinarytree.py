class Node:
    def __init__(self, val):

        self.val = val
        self.right = None
        self.left = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def inorderInsertion(self, val):
        self.root = self._inorderInsertion(self.root, val)

    def _insert(self, root, val):
        if root is None:
            return Node(val)

        currentNode = root
        parentNode = None
        while currentNode:
            parentNode = currentNode
            if val < currentNode.val:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        if val < parentNode.val:
            parentNode.left = Node(val)
        else:
            parentNode.right = Node(val)

        return root

    def _inorderInsertion(self, root, val):
        if root is None:
            return Node(val)

        currentNode = root
        stack = []

        while True:
            if currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left

            elif stack:
                currentNode = stack.pop()
                currentNode.val = val
                currentNode = currentNode.right
            else:
                break

        return root

    def inorderTraversal(self):

        currentNode = self.root
        stack = []

        while True:
            if currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left

            elif stack:
                currentNode = stack.pop()
                print(currentNode.val, end=" ")
                currentNode = currentNode.right
            else:
                break

    def search(self, val):
        currentNode = self.root
        parentNode = None
        while currentNode:
            parentNode = currentNode
            if val < currentNode.val:
                currentNode = currentNode.left
            elif val > currentNode.val:
                currentNode = currentNode.right
            else:
                return parentNode, currentNode
        else:
            return parentNode, None

    def lowestValue(self, root):
        currentNode = root
        while currentNode:
            currentNode = currentNode.left
        return currentNode

    def highestValue(self, root):
        currentNode = root
        while currentNode:
            currentNode = currentNode.right
        return currentNode

    def height(self):
        lheight = 0
        currentNode = self.root
        while currentNode:
            currentNode = currentNode.left
            lheight += 1
        rheight = 0
        currentNode = self.root
        while currentNode:
            currentNode = currentNode.right
            rheight += 1

        if lheight > rheight:
            return lheight
        else:
            return rheight


t = BinaryTree()
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in l:
    t.inorderInsertion(i)
t.inorderTraversal()
print()
print(t.height())
