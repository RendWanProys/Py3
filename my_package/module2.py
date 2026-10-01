def task2():
    Fin = open("../text_input.txt", "r", encoding="utf-8")
    Fout = open("../text_output.txt", "w", encoding="utf-8")

    words = []

    while True:
        s = Fin.readline()
        if not s:
            break
        for ch in '.,!?:;"()[]-—«»1234567890':
            s = s.replace(ch, " ")
        p = s.split()
        for w in p:
            words.append(w.lower())

    if words:
        min_len = len(words[0])
        for w in words:
            if len(w) < min_len:
                min_len = len(w)

        count = 0
        min_words = []
        for w in words:
            if len(w) == min_len:
                count += 1
                if w not in min_words:
                    min_words.append(w)

    else:
        count = 0
        min_words = []


    print("Самые короткие слова:", ", ".join(min_words))
    print("Встречаются раз:", count)

    Fout.write(f"Слова: {', '.join(min_words)}\n")
    Fout.write(f"Количество: {count}\n")

    Fin.close()
    Fout.close()

task2()