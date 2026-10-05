from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, TypeVar

T = TypeVar("T")


@dataclass
class _Node(Generic[T]):
    value: T
    next: _Node[T] | None = None


class LinkedList(Generic[T]):
    """Singly linked list with O(1) append (tail pointer) and in-place reversal."""

    def __init__(self, items=()) -> None:
        self._head: _Node[T] | None = None
        self._tail: _Node[T] | None = None
        self._size = 0
        for x in items:
            self.append(x)

    def append(self, value: T) -> None:
        node = _Node(value)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def prepend(self, value: T) -> None:
        self._head = _Node(value, self._head)
        if self._tail is None:
            self._tail = self._head
        self._size += 1

    def remove(self, value: T) -> bool:
        prev, cur = None, self._head
        while cur is not None:
            if cur.value == value:
                if prev is None:
                    self._head = cur.next
                else:
                    prev.next = cur.next
                if cur is self._tail:
                    self._tail = prev
                self._size -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def reverse(self) -> None:
        prev, cur = None, self._head
        self._tail = self._head
        while cur is not None:
            cur.next, prev, cur = prev, cur, cur.next
        self._head = prev

    def __iter__(self) -> Iterator[T]:
        cur = self._head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def __len__(self) -> int:
        return self._size
