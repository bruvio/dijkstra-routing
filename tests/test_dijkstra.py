def test_dijkstra(graph):
    result = graph.dijkstra("a", "e")

    assert result == 26
