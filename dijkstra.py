import heapq

def dijkstra(graf, start):
    dystans = {w: float('inf') for w in graf}
    dystans[start] = 0
    kolejka = [(0, start)]
    poprzednik = {w: None for w in graf}

    while kolejka:
        obecny_dystans, obecny_wierzcholek = heapq.heappop(kolejka)
        if obecny_dystans > dystans[obecny_wierzcholek]:
            continue
        for sasiad, waga in graf[obecny_wierzcholek]:
            odleglosc = obecny_dystans + waga
            if odleglosc < dystans[sasiad]:
                dystans[sasiad] = odleglosc
                poprzednik[sasiad] = obecny_wierzcholek
                heapq.heappush(kolejka, (odleglosc, sasiad))

    return dystans, poprzednik

def test():
    graf = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 5), ('D', 10)],
        'C': [('E', 3)],
        'D': [],
        'E': [('D', 4)]
    }
    dystans, poprzednik = dijkstra(graf, 'A')
    print(f"Dystans to: {dystans}")
    print(f"Poprzednik: {poprzednik}")

test()
