""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


# def check_binary_search_tree_(node):
#     return (_check_binary_search_tree_(node, -float("inf"), float("inf")))


# def _check_binary_search_tree_(node, mini, maxi):

#     # An empty tree is BST
#     if node is None:
#         return True

#     if node.data < mini or node.data > maxi:
#         return False

#     return (_check_binary_search_tree_(node.left, mini, node.data - 1) and
#             _check_binary_search_tree_(node.right, node.data + 1, maxi))


def check_binary_search_tree_(root):

    currentNode = root
    stack = []
    prev = -float("inf")

    while True:
        if currentNode:
            stack.append(currentNode)
            currentNode = currentNode.left

        elif stack:
            currentNode = stack.pop()
            if currentNode.data <= prev:
                return False
            else:
                prev = currentNode.data
            currentNode = currentNode.right
        else:
            return True
