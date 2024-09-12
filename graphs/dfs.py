from collections import deque

def main():
    graph = {
        "A": ["B", "C"],
        "B": ["C"],
        "C": ["D"],
        "D": []
    }

    dfs(graph, "A")


def dfs(graph, start_node):
    converted_graph = {k: deque(v) for k, v in graph.items()}
    node_stack = deque()
    visited_node_set = set()

    current_node = start_node
    print(start_node)
    visited_node_set.add(current_node)
    node_stack.append(current_node)

    while len(node_stack):
        if len(converted_graph[node_stack[-1]]) == 0:
            node_stack.pop()
        else:
            current_node = converted_graph[node_stack[-1]].pop()
            if current_node not in visited_node_set:
                print(current_node)
                visited_node_set.add(current_node)
                node_stack.append(current_node)


if __name__ == "__main__":
    main()
