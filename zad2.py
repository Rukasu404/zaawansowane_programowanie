def zad2(list):

    for i in list:
        i = i * 2
        print(i)


list1 = [1, 2, 3, 4, 5]
zad2(list1)


def zad2_2(list):
    wynik = [i * 2 for i in list]

    print(wynik)


zad2_2(list1)
