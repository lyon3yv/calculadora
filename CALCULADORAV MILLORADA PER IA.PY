# ---------- Colors (només estètica) ----------
RESET = "\033[0m"
NEGRETA = "\033[1m"
CIAN = "\033[96m"
VERD = "\033[92m"
GROC = "\033[93m"
VERMELL = "\033[91m"
MAGENTA = "\033[95m"
BLAU = "\033[94m"

print(f"""{CIAN}{NEGRETA}
╔═══════════════════════════════════════════════╗
║                                               ║
║            🧮  C A L C U L A D O R A          ║
║                                               ║
╠═══════════════════════════════════════════════╣
║                                               ║
║   {GROC}1{CIAN}  ➕  Sumar                                ║
║   {GROC}2{CIAN}  ➖  Restar                               ║
║   {GROC}3{CIAN}  ✖️   Multiplicar                          ║
║   {GROC}4{CIAN}  ➗  Dividir                              ║
║   {GROC}5{CIAN}  ▭   Àrea d'un rectangle                  ║
║   {GROC}6{CIAN}  ◯   Àrea d'un cercle                     ║
║   {GROC}7{CIAN}  📐  Equació lineal (ax + b = 0)          ║
║   {GROC}8{CIAN}  🚪  Sortir                               ║
║                                               ║
╚═══════════════════════════════════════════════╝{RESET}
""")
funcionar = True
while funcionar:
    opcio = int(input(f"{MAGENTA}{NEGRETA}👉 Escull una opció (1-8): {RESET}"))
    if opcio == 1:
        print(f"\n{BLAU}{NEGRETA}━━━━━━━━━━  ➕  SUMA  ━━━━━━━━━━{RESET}")
        n1 = float(input("  🔹 Primer nombre: "))
        n2 = float(input("  🔹 Segon nombre: "))
        resultat = n1 + n2
        print(f"\n  {VERD}{NEGRETA}✅ El resultat de la suma és:{RESET}", resultat)
    elif opcio == 2:
        print(f"\n{BLAU}{NEGRETA}━━━━━━━━━━  ➖  RESTA  ━━━━━━━━━━{RESET}")
        n1 = float(input("  🔹 Primer nombre: "))
        n2 = float(input("  🔹 Segon nombre: "))
        resultat = n1 - n2
        print(f"\n  {VERD}{NEGRETA}✅ El resultat de la resta és:{RESET}", resultat)
    elif opcio == 3:
        print(f"\n{BLAU}{NEGRETA}━━━━━━━━  ✖️  MULTIPLICACIÓ  ━━━━━━━━{RESET}")
        n1 = float(input("  🔹 Primer nombre: "))
        n2 = float(input("  🔹 Segon nombre: "))
        resultat = n1 * n2
        print(f"\n  {VERD}{NEGRETA}✅ El resultat de la multiplicació és:{RESET}", resultat)
    elif opcio == 4:
        print(f"\n{BLAU}{NEGRETA}━━━━━━━━━━  ➗  DIVISIÓ  ━━━━━━━━━━{RESET}")
        dividend = float(input("  🔹 Dividit: "))
        divisor = float(input("  🔹 Divisor: "))
        if divisor == 0:
            print(f"\n  {VERMELL}{NEGRETA}❌ Error: no es pot dividir entre zero.{RESET}")
        else:
            resultat = dividend / divisor
            print(f"\n  {VERD}{NEGRETA}✅ El resultat de la divisió és:{RESET}", resultat)
    elif opcio == 5:
        print(f"\n{BLAU}{NEGRETA}━━━━━━━━  ▭  ÀREA DEL RECTANGLE  ━━━━━━━━{RESET}")
        base = float(input("  🔹 Base: "))
        altura = float(input("  🔹 Altura: "))
        area = base * altura
        print(f"\n  {VERD}{NEGRETA}✅ L'àrea del rectangle és:{RESET}", area)
    elif opcio == 6:
        print(f"\n{BLAU}{NEGRETA}━━━━━━━━  ◯  ÀREA DEL CERCLE  ━━━━━━━━{RESET}")
        radi = float(input("  🔹 Radi: "))
        pi = 3.1416
        area = pi * radi * radi
        print(f"\n  {VERD}{NEGRETA}✅ L'àrea del cercle és:{RESET}", area)
    elif opcio == 7:
        print(f"\n{BLAU}{NEGRETA}━━━━━━  📐  EQUACIÓ LINEAL ax + b = 0  ━━━━━━{RESET}")
        a = float(input("  🔹 Valor de a: "))
        b = float(input("  🔹 Valor de b: "))
        if a == 0:
            print(f"\n  {GROC}{NEGRETA}⚠️  Si a = 0, l'equació no té solució única.{RESET}")
        else:
            x = -b / a
            print(f"\n  {VERD}{NEGRETA}✅ La solució és x ={RESET}", x)
    elif opcio == 8:
        print(f"\n{CIAN}{NEGRETA}👋 Fins aviat! Gràcies per fer servir la calculadora.{RESET}")
        funcionar = False
    else:
        print(f"\n  {VERMELL}{NEGRETA}❌ Opció no vàlida. Tria un nombre de l'1 al 8.{RESET}")
    print(f"\n{CIAN}─────────────────────────────────────────────────{RESET}\n")
