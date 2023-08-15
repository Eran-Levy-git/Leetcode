class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to hold elements
        self.min_stack = []  # Auxiliary stack to hold minimum elements

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if self.stack:
            popped_value = self.stack.pop()
            if popped_value == self.min_stack[-1]:
                self.min_stack.pop()
            return popped_value

    def top(self):
        if self.stack:
            return self.stack[-1]

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]


# Example usage
stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)

print(stack.get_min())  # Output: 1

stack.pop()
print(stack.get_min())  # Output: 2
