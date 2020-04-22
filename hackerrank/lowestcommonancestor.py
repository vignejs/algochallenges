import sys


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
    def __init__(self,info):
        self.info = info
        self.left = None
        self.right = None

this is a node of the tree, which contains info as data, left, right
'''


def search(root, val):
    currentNode = root
    parentNode = None
    pstack = []
    level = 0
    while currentNode:
        parentNode = currentNode
        pstack.append(parentNode)
        if val < currentNode.info:
            currentNode = currentNode.left
            level += 1
        elif val > currentNode.info:
            currentNode = currentNode.right
            level += 1
        else:
            return pstack, currentNode, level + 1


def lca(root, v1, v2):
    # Enter your code here
    pstack1, currentNode1, level1 = search(root, v1)
    pstack2, currentNode2, level2 = search(root, v2)
    while level1 != level2:
        if level1 > level2:
            pstack1.pop()
            level1 -= 1
        else:
            pstack2.pop()
            level2 -= 1
    while pstack1[-1] != pstack2[-1]:
        pstack1.pop()
        pstack2.pop()
    return pstack1[-1]


sys.stdin = open('in', 'r')

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
