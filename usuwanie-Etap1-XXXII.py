def roz1():
    fin_score = 0
    a, b = input().split()
    aint = int(a)
    bint = int(b)

    pula = list(range(aint, bint + 1))
    used = set()

    for i in range(len(pula)):
        if i in used:
            continue
        for j in range(i + 1, len(pula)):
            if j in used:
                continue
            if (pula[i] + pula[j]) % 2 == 0:
                used.add(i)
                used.add(j)
                fin_score += 2

    print(fin_score)
def roz2():
    fin_score = 0
    a, b = input().split()
    aint = int(a)
    bint = int(b)
    even_count = (bint // 2) - ((aint - 1) // 2) 
    odd_count = (bint - aint + 1) - even_count
    if even_count % 2 == 0 and odd_count % 2 == 0:
        fin_score += odd_count + even_count
    elif even_count % 2 == 0 and odd_count % 2 != 0:
        fin_score += even_count + odd_count - 1
    elif even_count % 2 != 0 and odd_count % 2 == 0:
        fin_score += even_count - 1 + odd_count
    elif even_count % 2 != 0 and odd_count %2 != 0:
        fin_score += even_count -1 + odd_count - 1
    print(fin_score)

def main():
    roz2()


main()
