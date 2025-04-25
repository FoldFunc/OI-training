from collections import defaultdict

# Algorytm Tarjana
def tarjans(graph, V):
    low = [-1] * V
    disc = [-1] * V
    stack = []
    in_stack = [False] * V
    sccs = []
    time = [0]  # Tylko po to, aby śledzić czas

    def dfs(u):
        disc[u] = low[u] = time[0]
        time[0] += 1
        stack.append(u)
        in_stack[u] = True
        
        for v in graph[u]:
            if disc[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:
                low[u] = min(low[u], disc[v])
        
        # Sprawdzamy, czy znaleźliśmy SCC
        if low[u] == disc[u]:
            component = []
            while True:
                v = stack.pop()
                in_stack[v] = False
                component.append(v)
                if v == u:
                    break
            sccs.append(component)
    
    # DFS dla wszystkich wierzchołków
    for i in range(V):
        if disc[i] == -1:
            dfs(i)
    
    return sccs

