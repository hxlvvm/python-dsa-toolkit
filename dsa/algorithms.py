"""Searching, sorting and graph algorithms, each with its complexity."""
import heapq
from collections import deque


def binary_search(items: list, target) -> int:
    """Index of target in a sorted list, or -1. O(log n)."""
    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def merge_sort(items: list) -> list:
    """Stable O(n log n) sort; returns a new list."""
    if len(items) <= 1:
        return list(items)
    mid = len(items) // 2
    left, right = merge_sort(items[:mid]), merge_sort(items[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    return out + left[i:] + right[j:]


def bfs_shortest_path(graph: dict, start, goal) -> list | None:
    """Fewest-edges path in an unweighted graph (adjacency dict). O(V + E)."""
    prev, seen, q = {}, {start}, deque([start])
    while q:
        node = q.popleft()
        if node == goal:
            path = [node]
            while node in prev:
                node = prev[node]
                path.append(node)
            return path[::-1]
        for nxt in graph.get(node, ()):
            if nxt not in seen:
                seen.add(nxt); prev[nxt] = node; q.append(nxt)
    return None


def dijkstra(graph: dict, start) -> dict:
    """Shortest distances from start in a graph with non-negative weights {u: [(v, w), ...]}. O((V + E) log V)."""
    dist, heap = {start: 0}, [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float("inf")):
            continue
        for v, w in graph.get(u, ()):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Indices of two numbers adding up to target, using a hash map. O(n)."""
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return seen[target - x], i
        seen[x] = i
    return None
