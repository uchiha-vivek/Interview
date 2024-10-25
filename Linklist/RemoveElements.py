class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()  # For a newline after printing all elements

class Solution:
    def removeElements(self, head: Node, val: int) -> Node:
        dummy = Node(next=head)
        prev, curr = dummy, head
        while curr:
            nxt = curr.next
            if curr.item == val:  # Use item instead of val
                prev.next = nxt
            else:
                prev = curr
            curr = nxt
        return dummy.next

# Example usage
mylist = SLL()
mylist.insert_at_start(40)
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_start(10)

print("Original List:")
mylist.print_list()

# Remove elements with value 20
solution = Solution()
mylist.start = solution.removeElements(mylist.start, 20)

print("List after removing elements with value 20:")
mylist.print_list()
