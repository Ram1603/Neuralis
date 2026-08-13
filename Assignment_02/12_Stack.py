class MinStack:

    def __init__(self):
        # We will store pairs: [number, minimum_so_far]
        self.stack = []

    def push(self, val: int) -> None:
        # If stack is empty, val is the minimum
        if not self.stack:
            self.stack.append((val, val))
        else:
            # Current min is the smaller of val or the previous minimum
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        # Return the value at the top of the stack
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the minimum stored with the top item
        return self.stack[-1][1]


#