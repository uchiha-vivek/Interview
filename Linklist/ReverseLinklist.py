class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL: 
    def __init__(self,start=None):
        self.start=start
    def is_empty(self,start=None):
        return self.start==None
    def insert_at_start(self,data):
        # creating a new node
        n=Node(data,self.start)
        self.start=n
    def print_list(self):
        temp=self.start   
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next


class Solution:
    def reverseList(self,head):
        prev,curr = None,head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
    

mylist = SLL()
mylist.insert_at_start(40)
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.print_list()
print("\n")

solution = Solution()
mylist.start = solution.reverseList(mylist.start)
print("After reversing linklist itereatively")
mylist.print_list()

 