from collections import deque


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["C"],
        "C": ["D"],
        "D": []
    }

    bfs(graph, "A")


def bfs(graph, start_node):
    node_queue = deque()
    visited_node_set = set()

    current_node = start_node
    print(current_node)
    visited_node_set.add(current_node)
    for adjacent_node in graph[current_node]:
        node_queue.append(adjacent_node)

    while len(node_queue) != 0:
        current_node = node_queue.popleft()
        if current_node not in visited_node_set:
            print(current_node)
            visited_node_set.add(current_node)
            for adjacent_node in graph[current_node]:
                node_queue.append(adjacent_node)


if __name__ == "__main__":
    main()
