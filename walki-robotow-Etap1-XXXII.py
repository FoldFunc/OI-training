def roz1():
    n = int(input())
    hash_map = {}
    for i in range(n):
        s, z = input().split()
        sint = int(s)
        zint = int(z)
        hash_map[sint] = zint
    used = {}
    for key, value in hash_map.items():
        if key in used and value in used:
            continue
        for keyj, valuej in hash_map.items():
            if keyj in used and valuej in used:
                continue

def main():
    roz1()


main()
