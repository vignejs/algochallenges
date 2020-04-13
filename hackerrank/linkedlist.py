class Node:
    def __init__(self, data: object) -> object:
        self.data = data
        self.next = None


class Solution:
    @staticmethod
    def display(head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        if not head:
            head = Node(data)
            return head
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
