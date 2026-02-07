"""
Breadth-First Search (BFS) Algorithm Implementation

Breadth-First Search is a graph traversal algorithm that explores vertices
in the order of their distance from the source vertex. It visits all vertices
at the present depth level before moving on to vertices at the next depth level.

Algorithm Description:
1. Start from the source vertex and mark it as visited.
2. Use a queue to keep track of vertices to be visited.
3. While the queue is not empty:
   a. Dequeue a vertex from the front of the queue.
   b. Visit all its adjacent vertices that haven't been visited yet.
   c. Mark them as visited and enqueue them.
4. Repeat until all reachable vertices are visited.

Applications:
- Finding the shortest path in unweighted graphs
- Web crawling
- Social network analysis
- Finding connected components in graphs
- Solving puzzles like mazes
"""

from collections import deque
from typing import Dict, List, Set, Optional


def breadth_first_search(graph: Dict[str, List[str]], start_node: str) -> List[str]:
    """
    Perform Breadth-First Search traversal on a graph.

    Args:
        graph: A dictionary representing the adjacency list of the graph.
               Keys are vertex labels, values are lists of adjacent vertices.
        start_node: The vertex from which to start the BFS traversal.

    Returns:
        A list of vertices in the order they were visited during BFS.

    Raises:
        ValueError: If start_node is not in the graph.

    Example:
        >>> graph = {
        ...     'A': ['B', 'C'],
        ...     'B': ['A', 'D', 'E'],
        ...     'C': ['A', 'F'],
        ...     'D': ['B'],
        ...     'E': ['B', 'F'],
        ...     'F': ['C', 'E']
        ... }
        >>> bfs_result = breadth_first_search(graph, 'A')
        >>> print(bfs_result)
        ['A', 'B', 'C', 'D', 'E', 'F']
    """
    if start_node not in graph:
        raise ValueError(f"Start node '{start_node}' not found in graph")

    # Initialize visited set and result list
    visited: Set[str] = set()
    result: List[str] = []

    # Use deque as a queue for efficient O(1) operations
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        # Dequeue the vertex from the front of the queue
        current_vertex = queue.popleft()
        result.append(current_vertex)

        # Visit all adjacent vertices
        for neighbor in graph.get(current_vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def bfs_shortest_path(graph: Dict[str, List[str]], start: str, target: str) -> Optional[List[str]]:
    """
    Find the shortest path between two vertices using BFS.

    Args:
        graph: Adjacency list representation of the graph.
        start: Starting vertex.
        target: Target vertex.

    Returns:
        List of vertices representing the shortest path from start to target,
        or None if no path exists.

    Example:
        >>> graph = {
        ...     'A': ['B', 'C'],
        ...     'B': ['A', 'D', 'E'],
        ...     'C': ['A', 'F'],
        ...     'D': ['B'],
        ...     'E': ['B', 'F'],
        ...     'F': ['C', 'E']
        ... }
        >>> path = bfs_shortest_path(graph, 'A', 'F')
        >>> print(path)
        ['A', 'C', 'F']
    """
    if start not in graph or target not in graph:
        return None

    if start == target:
        return [start]

    # Queue stores tuples of (vertex, path)
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        current_vertex, path = queue.popleft()

        for neighbor in graph.get(current_vertex, []):
            if neighbor == target:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


def bfs_connected_components(graph: Dict[str, List[str]]) -> List[List[str]]:
    """
    Find all connected components in a graph using BFS.

    Args:
        graph: Adjacency list representation of the graph.

    Returns:
        List of connected components, where each component is a list of vertices.

    Example:
        >>> graph = {
        ...     'A': ['B', 'C'],
        ...     'B': ['A', 'C'],
        ...     'C': ['A', 'B'],
        ...     'D': ['E'],
        ...     'E': ['D'],
        ...     'F': []
        ... }
        >>> components = bfs_connected_components(graph)
        >>> print(components)
        [['A', 'B', 'C'], ['D', 'E'], ['F']]
    """
    visited: Set[str] = set()
    components: List[List[str]] = []

    for vertex in graph:
        if vertex not in visited:
            # Perform BFS starting from this unvisited vertex
            component: List[str] = []
            queue = deque([vertex])
            visited.add(vertex)

            while queue:
                current = queue.popleft()
                component.append(current)

                for neighbor in graph.get(current, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            components.append(component)

    return components


def test_bfs_algorithm() -> None:
    """Test function to demonstrate the BFS algorithm."""
    # Example graph from the docstring
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("Testing BFS traversal:")
    bfs_result = breadth_first_search(graph, 'A')
    print(f"BFS traversal from 'A': {bfs_result}")
    print()

    print("Testing shortest path finding:")
    shortest_path = bfs_shortest_path(graph, 'A', 'F')
    print(f"Shortest path from 'A' to 'F': {shortest_path}")
    print()

    print("Testing connected components:")
    # Create a graph with disconnected components
    disconnected_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B'],
        'D': ['E'],
        'E': ['D'],
        'F': []
    }
    components = bfs_connected_components(disconnected_graph)
    print(f"Connected components: {components}")


if __name__ == "__main__":
    test_bfs_algorithm()


# Algorithm Complexity Analysis
# ============================
#
# Time Complexity: O(V + E)
# Where V is the number of vertices and E is the number of edges.
# Explanation:
# - Each vertex is enqueued and dequeued exactly once: O(V)
# - Each edge is examined exactly once when checking neighbors: O(E)
# - Total: O(V + E)
#
# Space Complexity: O(V)
# Explanation:
# - Visited set stores all vertices: O(V)
# - Queue can contain up to V vertices in the worst case: O(V)
# - Result list stores all vertices: O(V)
# - Total: O(V)
#
# Key Characteristics:
# 1. BFS finds the shortest path in unweighted graphs
# 2. It uses a queue (FIFO) data structure
# 3. It explores all vertices at the current depth before moving deeper
# 4. It is complete (will find a solution if one exists) and optimal
#    (finds the shortest path) for unweighted graphs
#
# References:
# - Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). 
#   Introduction to Algorithms (3rd ed.). MIT Press.
# - Breadth-first search algorithm fundamentals and analysis