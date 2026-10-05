from collections import deque


class Stack:
    """LIFO stack on a Python list (amortised O(1) push/pop)."""

    def __init__(self) -> None:
        self._items: list = []

    def push(self, x) -> None:
        self._items.append(x)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)


class Queue:
    """FIFO queue on collections.deque (O(1) at both ends)."""

    def __init__(self) -> None:
        self._items: deque = deque()

    def enqueue(self, x) -> None:
        self._items.append(x)

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def __len__(self) -> int:
        return len(self._items)


def balanced_brackets(text: str) -> bool:
    """Classic stack exercise: are (), [] and {} balanced?"""
    pairs, s = {")": "(", "]": "[", "}": "{"}, Stack()
    for ch in text:
        if ch in "([{":
            s.push(ch)
        elif ch in pairs:
            if not len(s) or s.pop() != pairs[ch]:
                return False
    return len(s) == 0
