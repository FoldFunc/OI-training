def floyd_warshall(graf):
    n = len(graf)
    d = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        d[i][i]
    for u in range(n):
        for v, waga in graf[u]:
            d[u][v] = waga
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]


    return d


def test():
        # Example graph with 4 nodes: 0, 1, 2, 3
    # Each node points to a list of (neighbor, weight)
    graph = [
        [(1, 5), (3, 10)],     # edges from node 0
        [(2, 3)],              # edges from node 1
        [(3, 1)],              # edges from node 2
        [],                    # node 3 has no outgoing edges
    ]
    shortest_paths = floyd_warshall(graph)

    print("All pairs shortest paths:")
    for row in shortest_paths:
        print(row)


test()
