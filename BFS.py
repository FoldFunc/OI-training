from collections import deque

def bfs(graf, start):
    ilosc_poloczonych = 0
    odwiedzenie = set()
    kolejka = deque([start])
    odwiedzenie.add(start)

    while kolejka:
        wierzcholek = kolejka.popleft()
        print(wierzcholek)
        ilosc_poloczonych += 1
        for sasiad in graf[wierzcholek]:
            if sasiad not in odwiedzenie:
                kolejka.append(sasiad)
                odwiedzenie.add(sasiad)

    if ilosc_poloczonych < len(graf):
        return 1
    return 0
graf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
grafroz = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': []
}
print(bfs(graf, 'A'))
print(bfs(grafroz, 'A'))

