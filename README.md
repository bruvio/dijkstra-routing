# Dijkstra's algorithm implementation

In this repo I implement a simple Dijkstra's algorithm.
to test, in the repo is also present a data file representing a graph of walkable streets.

The data file contains a list of Open Street Maps (OSM) ids that are contained in the street graph, followed by a list of bidirectional edges, with distances between them given in meters. The edges represent the walkable streets in the graph.

```
<number of nodes>
<OSM id of node>
...
<OSM id of node>
<number of edges>
<from node OSM id>
<to node OSM id> <length in meters>
...
<from node OSM id> <to node OSM id> <length in meters>
```

The program takes a graph using this representation as input, and computes the shortest walking distance in meters between two given OSM nodes in the graph (assuming all edges are walkable). For example:

```
./run.sh test-graph.dat 876500321 1524235806
2709
```

### 1. Initial Setup

**Quick Setup** (prereq: `git, python3.8` )

```bash
unzip xxxx.zip
python -m venv .env3.8

```

#### Project Structure:

Mono-repo style

```
├── pytest.ini
├── README.md
├── requirements-dev.txt
├── requirements.txt
├── run.sh
├── shortestpath.py
├── test-graph.dat
├── tests
│   ├── conftest.py
│   ├── __init__.py
│   └── test_dijkstra.py
└── utils.py

```

- `/tests/`: tests for basic operations on the app.
- `utils.py`: help functions
- `test-graph.dat`: input dataset
- `shortestpath.py`: main file
- `run.sh`: script to run the program

## The algorithm

1.  Mark all nodes unvisited and store them.
2.  Set the distance to zero for our initial node and to infinity for other nodes.
3.  Select the unvisited node with the smallest distance, it's current node now.
4.  Find unvisited neighbors for the current node and calculate their distances through the current node. Compare the newly calculated distance to the assigned and save the smaller one. For example, if the node A has a distance of 6, and the A-B edge has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8.
5.  Mark the current node as visited and remove it from the unvisited set.
6.  Stop, if the destination node has been visited (when planning a route between two specific nodes) or if the smallest distance among the unvisited nodes is infinity. If not, repeat steps 3-6.

## Implementation

I use namedtuple for storing edge data and deque.

After reading the file I create the Graph adding vertices andproperties: adding, removing and finding neighbors functionalities.

I also created a simple test with a little example to see if the algorithm is correct.
