# Python DSA Toolkit

Core data structures and algorithms implemented from scratch in Python, with type hints, docstrings that state
the complexity, and tests. Built as interview practice.

| Module | Contents |
|---|---|
| `dsa/linked_list.py` | Generic singly linked list: O(1) append with a tail pointer, remove, in-place reverse |
| `dsa/stack_queue.py` | Stack (list) and Queue (deque); balanced-brackets checker |
| `dsa/lru_cache.py` | LRU cache with O(1) get/put (hash map + ordered linked list) |
| `dsa/algorithms.py` | Binary search, merge sort, BFS shortest path, Dijkstra, two-sum with a hash map |

## Test
```bash
pip install -r requirements.txt
pytest -q
```

## Next steps
- Heap and trie implementations
- Dynamic programming (knapsack, edit distance)
- Benchmarks against the standard library
