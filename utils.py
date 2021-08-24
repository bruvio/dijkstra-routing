import logging
from collections import deque, namedtuple

logger = logging.getLogger(__name__)
# use infinity as a default distance to nodes.
inf = float("inf")
Edge = namedtuple("Edge", "start, end, cost")


def make_edge(start, end, cost=1):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError("Wrong edges data: {}".format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(sum(([edge.start, edge.end] for edge in self.edges), []))

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError("Edge {} {} already exists".format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    # @property
    # def neighbours(self):
    #     neighbours = {vertex: set() for vertex in self.vertices}
    #     for edge in self.edges:
    #         neighbours[edge.start].add((edge.end, edge.cost))

    #     return neighbours

    # use the following if the graph is undirected / bidirectional
    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))
            neighbours[edge.end].add((edge.start, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, "Such source node doesn't exist"
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {vertex: None for vertex in self.vertices}
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(vertices, key=lambda vertex: distances[vertex])
            logger.debug("current vertex is {}".format(current_vertex))
            vertices.remove(current_vertex)
            if (distances[current_vertex] == inf) or (current_vertex == dest):
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        logger.debug("path to destination is \n")

        while path:
            value = path.popleft()
            logger.debug("{} \n".format(value))

        return distances[dest]


class MinHeap:
    def __init__(self, array):
        # print(array)
        # Do not edit the line below.
        self.vertexMap = {idx: idx for idx in range(len(array))}
        self.heap = self.buildHeap(array)

    def isEmpty(self):
        return len(self.heap) == 0

    # O(N) time and O(1) space
    def buildHeap(self, array):
        # Write your code here.
        firstParent = (len(array) - 2) // 2
        for currentIndex in reversed(range(firstParent + 1)):
            self.siftDown(currentIndex, len(array) - 1, array)
            # print(array)
        return array

    # O(log(n)) time and O(1) space
    def siftDown(self, start, endIdx, heap):
        # Write your code here.
        childOneIdx = start * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = start * 2 + 2 if start * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap][1] < heap[start][1]:
                self.swap(start, idxToSwap, heap)
                start = idxToSwap
                childOneIdx = start * 2 + 1
            else:
                return

    # O(log(n)) time and O(1) space
    def siftUp(self, start, heap):
        # Write your code here.
        parentIdx = (start - 1) // 2
        while start > 0 and heap[start][1] < heap[parentIdx][1]:
            self.swap(start, parentIdx, heap)
            start = parentIdx
            parentIdx = (start - 1) // 2

    def swap(self, i, j, array):
        self.vertexMap[array[i][0]] = j
        self.vertexMap[array[j][0]] = i
        array[i], array[j] = array[j], array[i]

    # O(log(n)) time and O(1) space
    def remove(self):
        # Write your code here.
        self.swap(0, len(self.heap) - 1, self.heap)
        vertex, distance = self.heap.pop()
        self.vertexMap.pop(vertex)
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return vertex, distance

    def update(self, vertex, value):
        self.heap[self.vertexMap[vertex]] = (vertex, value)
        self.siftUp(self.vertexMap[vertex], self.heap)


def dijkstrasAlgorithm(start, dest, edges):
    """[summary]

    Args:
        start ([int]): [start node ]
        dest ([int]): [destination node]
        edges ([list]): [adjacency list that has the same lenght of the number of nodes/vertices of the graph]

    Returns:
        [int]: [minimum distance between start and dest]
    """
    distances = [float("inf")] * len(edges)
    distances[start] = 0
    minDistanceHeap = MinHeap([(idx, float("inf")) for idx in range(len(edges))])
    minDistanceHeap.update(start, 0)

    while not minDistanceHeap.isEmpty():
        nextVertex, minDistance = minDistanceHeap.remove()
        if minDistance == float("inf"):
            break
        for pair in edges[nextVertex]:
            destination = pair[0]
            distance = pair[1]
            pathLength = distances[nextVertex] + distance
            if pathLength < distances[destination]:
                distances[destination] = pathLength
                minDistanceHeap.update(destination, pathLength)

    for i, distance in enumerate(distances):
        if distance == float("inf"):
            distances[i] = -1

    return distances[dest]


def remap_nodes(vertices, neighbours):
    """given a list of vertices/nodes and a dictionary of neighbours, remaps the node names to integer using a hashtable and creates a adjacency list

    Args:
        vertices ([type]): [description]
        neighbours ([type]): [description]

    Returns:
        [type]: [adjacency list and hashtable that remaps the nodes]
    """
    hashmap = dict()
    for i in range(0, len(vertices)):
        hashmap[vertices[i]] = i

    edges = []

    for vertex in neighbours.keys():

        current_vertex = list(neighbours[vertex])

        remapped_vertex = []
        for current_tuple in current_vertex:
            remapped_tuple = tuple([hashmap[str(current_tuple[0])], current_tuple[1]])
            remapped_vertex.append(remapped_tuple)

        edge = [list(i) for i in remapped_vertex]

        edges.append(edge)
    return edges, hashmap
