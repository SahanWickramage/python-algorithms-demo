# python-algorithms-demo

## Graph algorithms

One data structure that can hold a graph is map (dictionary in python context) where key is a node and value is the list of adjacency nodes to it.

```python
my_graph = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["D"],
    "D": []
}
```

Graph traversal algorithms need two data structures. a queue for hold nodes that are to be visited and a set for hold node are already visited.

```python
node_queue = deque() # initialize queue
node_queue.append(adjacent_node) # enqueue elements
node_queue.popleft() # dequeue elements
len(node_queue) != 0 # is empty check

visited_node_set = set() # initialize set
visited_node_set.add(current_node) # add elements
current_node not in visited_node_set # check existence
```

