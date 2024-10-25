class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start == None

    def insert_at_first(self, data):
        n = Node(data, self.start)
        self.start = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()

class Solution:
    # def isPallindrome(self, head: Node) -> bool:
    #     nums = []
    #     while head:
    #         nums.append(head.item)
    #         head = head.next
    #     l, r = 0, len(nums) - 1
    #     while l <= r:
    #         if nums[l] != nums[r]:
    #             return False
    #         l += 1
    #         r -= 1  # Decrement r instead of increment
    #     return True
    def isPallindrome(self,head:Node)-> bool:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        # reverse second half
        prev=None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        # check pallindrome
        left,right=head,prev
        while right:
            if left.item != right.item:
                return False
            left=left.next
            right=right.next
        return True


# Example usage
mylist = SLL()
mylist.insert_at_first(40)
mylist.insert_at_first(30)
mylist.insert_at_first(30)
mylist.insert_at_first(40)
mylist.print_list()
print("\n")
solution = Solution()
is_palindrome = solution.isPallindrome(mylist.start)
print("Is the list a palindrome?\n", is_palindrome)
