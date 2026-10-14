def zad_5(list, a):

    wynik = False
    for i in range(0, len(list)):
        if list[i] == a:
            wynik = True
            break
    print(wynik)
    return wynik

list=[5,6,2,1,6,4,8]
zad_5(list, 0)