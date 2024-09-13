from dfs import dfs


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["C"],
        "C": ["D"],
        "D": []
    }

    topological_order = dfs(graph, "A")
    print(topological_order)


if __name__ == "__main__":
    main()
