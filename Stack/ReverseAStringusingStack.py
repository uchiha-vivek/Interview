## Reversing a string using stack

class Stack:
    def __init__(self):
        self.items = []
    def push (self,data):
        self.items.append(data)
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)
    
    def reverse(self,string):
        for char in string:
            self.push(char)
        reversed_string =""
        while not self.is_empty():
            reversed_string+= self.pop()
        return reversed_string




s = Stack()
input_string = "abc"
reversed_string = s.reverse(input_string)
print(reversed_string)

