def test_dijkstra(graph):
    result = graph.dijkstra("a", "e")
    print(result)
    assert result == 20
