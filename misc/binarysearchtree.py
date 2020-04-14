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

    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        print(root.val, end=" ")
        self.inorderTraversal(root.right)

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

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, root, val):
        parentNode, currentNode = self.search(val)
        if currentNode is None:
            print("node doest exist")
            return root

        if parentNode.left.val == val:
            parentNode.left = self._deleteNode(currentNode)
        else:
            parentNode.right = self._deleteNode(currentNode)

        return root

    def _deleteNode(self, node):
        if node.left is None and node.right is None:
            return None
        if node.left and node.right:
            inOrderSuccessor = self.deleteInOrderSuccessor(node)
            node.val = inOrderSuccessor.val
        elif node.left:
            node = node.left
        else:
            node = node.right

    def deleteInOrderSuccessor(self, node):
        parent = node
        node = node.right

        while node.left:
            parent = node
            node = node.left

        if node.left is None:
            parent.right = node.right
        else:
            parent.left = node.right

        node.right = None
        return node


t = BinaryTree()
t.insert(10)
t.insert(5)
t.insert(15)
t.insert(2)
t.insert(5)
t.inorderTraversal(t.root)
print()
t.search(5)
t.search(2)
t.search(12)
t.delete(10)
t.inorderTraversal(t.root)
