class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left
    def isEmpty(self) -> bool:
        return self.left.next == self.right
    
    def append(self, value: int) -> None:
        new = Node(value)
        last = self.right.prev

        last.next = new
        new.prev = last
        new.next = self.right
        self.right.prev = new

        
    def appendleft(self, value: int) -> None:
        new = Node(value)
        first = self.left.next

        self.left.next = new
        new.prev = self.left
        new.next = first
        first.prev = new

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        target = self.right.prev
        value = target.value
        prev_node = target.prev

        prev_node.next = self.right
        self.right.prev = prev_node

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        target = self.left.next
        value = target.value
        next_node = target.next
        self.left.next = next_node
        next_node.prev = self.left
    
        return value
        
        