import random

import pytest

from dsa.algorithms import bfs_shortest_path, binary_search, dijkstra, merge_sort, two_sum
from dsa.linked_list import LinkedList
from dsa.lru_cache import LRUCache
from dsa.stack_queue import Queue, Stack, balanced_brackets


def test_linked_list():
    ll = LinkedList([1, 2, 3])
    ll.prepend(0); ll.append(4)
    assert list(ll) == [0, 1, 2, 3, 4] and len(ll) == 5
    assert ll.remove(4) and not ll.remove(99)
    ll.reverse(); ll.append(-1)
    assert list(ll) == [3, 2, 1, 0, -1]


def test_lru_cache_evicts_least_recent():
    c = LRUCache(2)
    c.put("a", 1); c.put("b", 2); c.get("a"); c.put("c", 3)
    assert c.get("b") is None and c.get("a") == 1 and c.get("c") == 3
    with pytest.raises(ValueError):
        LRUCache(0)


def test_stack_queue_and_brackets():
    s, q = Stack(), Queue()
    for i in range(3):
        s.push(i); q.enqueue(i)
    assert s.pop() == 2 and q.dequeue() == 0
    assert balanced_brackets("{[()()]}") and not balanced_brackets("([)]") and not balanced_brackets("((")
    with pytest.raises(IndexError):
        Stack().pop()


def test_search_and_sort():
    data = random.Random(0).sample(range(1000), 200)
    s = merge_sort(data)
    assert s == sorted(data)
    assert binary_search(s, s[57]) == 57 and binary_search(s, 5000) == -1


def test_graphs_and_two_sum():
    g = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"]}
    assert bfs_shortest_path(g, "A", "E") in (["A", "B", "D", "E"], ["A", "C", "D", "E"])
    assert bfs_shortest_path(g, "E", "A") is None
    wg = {"A": [("B", 4), ("C", 1)], "C": [("B", 2)], "B": [("D", 1)]}
    assert dijkstra(wg, "A") == {"A": 0, "B": 3, "C": 1, "D": 4}
    assert two_sum([2, 7, 11, 15], 9) == (0, 1) and two_sum([1, 2], 10) is None
