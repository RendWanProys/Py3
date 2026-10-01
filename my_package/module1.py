def task1():
    Fin = open("../tovar_input.txt", "r", encoding="utf-8")
    Fout = open("../tovar_output.txt", "w", encoding="utf-8")

    tovar = input("Введите товар: ")
    sum = 0
    country = []

    while True:
        s = Fin.readline()
        if not s:
            break
        p = s.split()
        if len(p) >= 3:
            if p[0] == tovar:
                sum += int(p[2])
                if p[1] not in country:
                    country.append(p[1])

    print(sum)
    print(country)

    Fout.write(str(sum) + "\n")
    Fout.write(" ".join(country))

    Fin.close()
    Fout.close()
task1()