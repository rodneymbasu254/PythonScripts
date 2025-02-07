class Stack:
  def __init__(self, max_size):
    self.max_size = max_size
    self.arr = [None] * max_size
    self.top = -1

  def is_empty(self):
    return self.top == -1

  def is_full(self):
    return self.top == self.max_size - 1

  def push(self, data):
    if self.is_full():
      print("Stack Overflow")
    else:
      self.top += 1
      self.arr[self.top] = data

  def pop(self):
    if self.is_empty():
      print("Stack Underflow")
    else:
      removed_data = self.arr[self.top]
      self.top -= 1
      return removed_data

  def peek(self):
    if self.is_empty():
      print("Stack Underflow")
    else:
      return self.arr[self.top]

# Example usage
stack = Stack(5)
stack.push(10)
stack.push(20)
print(stack.peek())  # Output: 20
stack.pop()
print(stack.peek())  