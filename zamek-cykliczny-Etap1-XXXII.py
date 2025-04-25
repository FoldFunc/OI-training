from collections import deque
def rotate(x):
    s = str(x)
    rotated = s[1:] + s[0]
    return int(rotated.lstrip('0') or '0')
def minimal_presses(n):
    visited = set()
    queue = deque()
    queue.append((n, 0))
    visited.add(n)
    print("Hello world")
    while queue:
        current, steps = queue.popleft()

        if current == 1:
            return steps

        next_plus = current + 1
        if next_plus not in visited and next_plus < 10**6:
            visited.add(next_plus)
            queue.append((next_plus, steps + 1))

        next_rot = rotate(current)
        if next_rot not in visited:
            visited.add(next_rot)
            queue.append((next_rot, steps + 1))

n = int(input())
print(minimal_presses(n))

