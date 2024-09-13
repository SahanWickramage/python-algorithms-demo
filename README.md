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

Breadth first search algorithm need two data structures. a queue for hold nodes that are to be visited and a set for hold node are already visited.

```python
node_queue = deque() # initialize queue
node_queue.append(adjacent_node) # enqueue elements
node_queue.popleft() # dequeue elements
len(node_queue) != 0 # is empty check

visited_node_set = set() # initialize set
visited_node_set.add(current_node) # add elements
current_node not in visited_node_set # check existence
```

Depth first search algorithm need two data structures. a stack for hold nodes that are to be visited and a set for hold node are already visited.

```python
node_stack = deque() # initialize stack
node_stack.append(current_node) # push elements
node_stack.pop() # pop elements
node_stack[-1] # check last element without popping
```

Topological sort is forward or reversed depth first search based on the context. Topological sort gives the execution order of a dependent tasks