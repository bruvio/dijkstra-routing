from utils import dijkstrasAlgorithm


def test_dijkstra(graph):
    result = graph.dijkstra("a", "e")
    print(result)
    assert result == 20


def test_dijkstra_minheap():
    edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
    start = 0
    stop = 2
    min_distance = dijkstrasAlgorithm(start, stop, edges)
    assert 13 == min_distance
