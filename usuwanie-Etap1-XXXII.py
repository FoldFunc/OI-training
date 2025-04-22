def roz1():
    fin_score = 0
    a, b = input("").split()
    aint = int(a)
    bint = int(b)

    pula = []
    for i in range(aint, bint + 1):
        pula.append(i)


    for i in range(len(pula)):
        for j in range(len(pula)):
            if (pula[i] + pula[j]) % 2 == 0 and i != j and pula[i] != 0 and pula[j] != 0:
                pula[i] = 0
                pula[j] = 0
                fin_score += 2


    print(fin_score)
def roz2():
    pass


def main():
    roz1()


main()
