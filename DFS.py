def dfs(labirynt, x, y, cel_x, cel_y, odwiedzone, sciezka):
    if x < 0 or x >= len(labirynt) or y < 0 or y >= len(labirynt[0]):
        return False
    if labirynt[x][y] == 1 or odwiedzone[x][y]:
        return False

    odwiedzone[x][y] = True
    sciezka.append((x, y))
    if x == cel_x or y == cel_y:
        return True

    if (dfs(labirynt, x - 1, y, cel_x, cel_y, odwiedzone, sciezka) or
        dfs(labirynt, x + 1, y, cel_x, cel_y, odwiedzone, sciezka) or
        dfs(labirynt, x, y - 1, cel_x, cel_y, odwiedzone, sciezka) or
        dfs(labirynt, x, y + 1, cel_x, cel_y, odwiedzone, sciezka)):
        return True
    sciezka.pop()
    return False

def test():
    labirynt = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_x, start_y = 0, 0
    cel_x, cel_y = 4, 4
    odwiedzone = [[False for _ in range(len(labirynt[0]))] for _ in range(len(labirynt))]
    sciezka = []

    if dfs(labirynt, start_x, start_y, cel_x, cel_y, odwiedzone, sciezka):
        print("Znaleziono ścieżkę:")
        print(sciezka)
    else:
        print("Brak ścieżki do celu.")
test()

def dfs_graf(graf, start, end, odwiedzone, sciezka):
    odwiedzone[start] = True
    sciezka.append(start)
    if start == end:
        return True
    for sasiad in graf[start]:
        if not odwiedzone[sasiad]:
            if dfs_graf(graf, sasiad, end, odwiedzone, sciezka):
                return True
    sciezka.pop()
    return False

def test_graf():
    graf = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
    4: [0]
    }
    odwiedzone = [False] * len(graf)
    sciezka = []
    if dfs_graf(graf, 0, 4, odwiedzone, sciezka):
        print("Ścieżka istnieje:", sciezka)
    else:
        print("Brak ścieżki.")
test_graf()


