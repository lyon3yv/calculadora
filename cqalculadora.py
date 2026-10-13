print("""
=========================================
             CALCULADORA 
=========================================
Opcions:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Àrea d'un rectangle
6. Àrea d'un cercle
7. Equació lineal (ax + b = 0)
8. Sortir
=========================================
""")

funcionar = True

while funcionar:
    opcio = int(input("Escull una opció (1-8): "))

    if opcio == 1:
        print("--- SUMA ---")
        n1 = float(input("Primer nombre: "))
        n2 = float(input("Segon nombre: "))
        resultat = n1 + n2
        print("El resultat de la suma és:", resultat)

    elif opcio == 2:
        print("--- RESTA ---")
        n1 = float(input("Primer nombre: "))
        n2 = float(input("Segon nombre: "))
        resultat = n1 - n2
        print("El resultat de la resta és:", resultat)

    elif opcio == 3:
        print("--- MULTIPLICACIÓ ---")
        n1 = float(input("Primer nombre: "))
        n2 = float(input("Segon nombre: "))
        resultat = n1 * n2
        print("El resultat de la multiplicació és:", resultat)

    elif opcio == 4:
        print("--- DIVISIÓ ---")
        dividend = float(input("Dividit: "))
        divisor = float(input("Divisor: "))
        if divisor == 0:
            print("Error: no es pot dividir entre zero.")
        else:
            resultat = dividend / divisor
            print("El resultat de la divisió és:", resultat)

    elif opcio == 5:
        print("--- ÀREA DEL RECTANGLE ---")
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        area = base * altura
        print("L'àrea del rectangle és:", area)

    elif opcio == 6:
        print("--- ÀREA DEL CERCLE ---")
        radi = float(input("Radi: "))
        pi = 3.1416
        area = pi * radi * radi
        print("L'àrea del cercle és:", area)

    elif opcio == 7:
        print("--- EQUACIÓ LINEAL ax + b = 0 ---")
        a = float(input("Valor de a: "))
        b = float(input("Valor de b: "))
        if a == 0:
            print("Si a = 0, l'equació no té solució única.")
        else:
            x = -b / a
            print("La solució és x =", x)

    elif opcio == 8:
        print("Fins aviat! Gràcies per fer servir la calculadora.")
        funcionar = False

    else:
        print("Opció no vàlida. Tria un nombre de l'1 al 8.")

    print("-----------------------------------------")
