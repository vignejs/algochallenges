class Node:
    def __init__(self, p, q):

        self.p = p
        self.q = q
        try:
            self.val = p / q
        except ZeroDivisionError:
            self.val = float("inf")
        self.lparent = None
        self.rparent = None


class BinaryTree:

    def __init__(self):
        self.root = Node(1, 1)
        self.root.lparent = Node(0, 1)
        self.root.rparent = Node(1, 0)
        self.position = ""

    def search(self, p, q):
        val = p / q
        currentNode = self.root
        while True:
            if currentNode.p == p and currentNode.q == q:
                break
            else:
                if val < currentNode.val:
                    lparent = currentNode.lparent
                    rparent = currentNode
                    pcur = lparent.p + rparent.p
                    qcur = lparent.q + rparent.q
                    self.position += "L"
                    currentNode = Node(pcur, qcur)
                    currentNode.lparent = Node(lparent.p, lparent.q)
                    currentNode.rparent = Node(rparent.p, rparent.q)
                else:
                    lparent = currentNode
                    rparent = currentNode.rparent
                    pcur = lparent.p + rparent.p
                    qcur = lparent.q + rparent.q
                    self.position += "R"
                    currentNode = Node(pcur, qcur)
                    currentNode.lparent = Node(lparent.p, lparent.q)
                    currentNode.rparent = Node(rparent.p, rparent.q)

    def find(self, direction):
        currentNode = self.root
        for d in direction:
            if d == "L":
                lparent = currentNode.lparent
                rparent = currentNode
                pcur = lparent.p + rparent.p
                qcur = lparent.q + rparent.q
                currentNode = Node(pcur, qcur)
                currentNode.lparent = Node(lparent.p, lparent.q)
                currentNode.rparent = Node(rparent.p, rparent.q)
            else:
                lparent = currentNode
                rparent = currentNode.rparent
                pcur = lparent.p + rparent.p
                qcur = lparent.q + rparent.q
                currentNode = Node(pcur, qcur)
                currentNode.lparent = Node(lparent.p, lparent.q)
                currentNode.rparent = Node(rparent.p, rparent.q)
        return f"{currentNode.p}/{currentNode.q}"


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for _ in range(n):
    t = BinaryTree()
    line = input()
    lspilt = line.split("/")
    if len(lspilt) > 1:
        p = int(lspilt[0])
        q = int(lspilt[1])
        t.search(p, q)
        print(t.position)
    else:
        print(t.find(line))
