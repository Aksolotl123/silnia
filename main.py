import sys

def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

def silnia_rek(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")
    if n == 0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj argument silnii: "))
    print(f"Silnia z {n} wynosi: {silnia(n)}")
    sys.setrecursionlimit(9000000)
    print(f"Silnia rekurencyjna z {n} wynosi: {silnia_rek(n)}")
except ValueError as e:
    print(e)
except:
    print("mamy problem")
    raise