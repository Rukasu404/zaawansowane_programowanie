def zad3(a):

    parzysta = False

    if a % 2 == 0:
        parzysta = True

    return parzysta


liczba = 1
czy_parzysta = zad3(liczba)

if czy_parzysta is True:
    print("liczba parzysta")
else:
    print("liczba nieparzysta")
